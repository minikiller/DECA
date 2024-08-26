# -*- coding: utf-8 -*-
#
# Max-Planck-Gesellschaft zur Förderung der Wissenschaften e.V. (MPG) is
# holder of all proprietary rights on this computer program.
# Using this computer program means that you agree to the terms 
# in the LICENSE file included with this software distribution. 
# Any use not explicitly granted by the LICENSE is prohibited.
#
# Copyright©2019 Max-Planck-Gesellschaft zur Förderung
# der Wissenschaften e.V. (MPG). acting on behalf of its Max Planck Institute
# for Intelligent Systems. All rights reserved.
#
# For comments or questions, please email us at deca@tue.mpg.de
# For commercial licensing contact, please contact ps-license@tuebingen.mpg.de

import os
import cv2
import numpy as np
from time import time
from scipy.io import savemat
import argparse
import torch
from decalib.deca import DECA
from decalib.utils import util
from decalib.utils.config import cfg as deca_cfg
from decalib.datasets import datasets

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} 执行时间: {elapsed_time} 秒")
        return result
    return wrapper

@timer_decorator
def process_image(image_path, savefolder, device, use_tex, rasterizer_type, extract_tex, render_orig):
    # Create savefolder if it does not exist
    os.makedirs(savefolder, exist_ok=True)

    # Load the image
    testdata = datasets.TestData(image_path, iscrop=True, face_detector='fan')

    # Initialize DECA
    deca_cfg.model.use_tex = use_tex
    deca_cfg.rasterizer_type = rasterizer_type
    deca_cfg.model.extract_tex = extract_tex
    deca = DECA(config=deca_cfg, device=device)

    # Process the image
    data = testdata[0]
    name = data['imagename']
    image = data['image'].to(device)[None, ...]  # Add batch dimension

    with torch.no_grad():
        codedict = deca.encode(image)
        opdict, visdict = deca.decode(codedict)

        if render_orig:
            tform = data['tform'][None, ...]
            tform = torch.inverse(tform).transpose(1, 2).to(device)
            original_image = data['original_image'][None, ...].to(device)
            _, orig_visdict = deca.decode(codedict, render_orig=True, original_image=original_image, tform=tform)
            orig_visdict['inputs'] = original_image

    # Save results
    if args.saveDepth or args.saveKpt or args.saveObj or args.saveMat or args.saveImages:
        os.makedirs(os.path.join(savefolder, name), exist_ok=True)

    if args.saveDepth:
        depth_image = deca.render.render_depth(opdict['trans_verts']).repeat(1, 3, 1, 1)
        visdict['depth_images'] = depth_image
        cv2.imwrite(os.path.join(savefolder, name + '_depth.jpg'), util.tensor2image(depth_image[0]))

    if args.saveKpt:
        np.savetxt(os.path.join(savefolder, name + '_kpt2d.txt'), opdict['landmarks2d'][0].cpu().numpy())
        np.savetxt(os.path.join(savefolder, name + '_kpt3d.txt'), opdict['landmarks3d'][0].cpu().numpy())

    if args.saveObj:
        deca.save_obj(os.path.join(savefolder, name + '.obj'), opdict)

    if args.saveMat:
        opdict = util.dict_tensor2npy(opdict)
        savemat(os.path.join(savefolder, name + '.mat'), opdict)

    if args.saveVis:
        cv2.imwrite(os.path.join(savefolder, name + '_vis.jpg'), deca.visualize(visdict))
        if args.render_orig:
            cv2.imwrite(os.path.join(savefolder, name + '_vis_original_size.jpg'), deca.visualize(orig_visdict))

    if args.saveImages:
        for vis_name in ['inputs', 'rendered_images', 'albedo_images', 'shape_images', 'shape_detail_images', 'landmarks2d']:
            if vis_name in visdict.keys():
                image = util.tensor2image(visdict[vis_name][0])
                cv2.imwrite(os.path.join(savefolder, name + '_' + vis_name + '.jpg'), image)
                if args.render_orig:
                    image = util.tensor2image(orig_visdict[vis_name][0])
                    cv2.imwrite(os.path.join(savefolder, 'orig_' + name + '_' + vis_name + '.jpg'), image)

    print(f'-- 请检查结果在 {savefolder}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DECA: Detailed Expression Capture and Animation')

    parser.add_argument('-i', '--inputpath', default='TestSamples/examples', type=str,
                        help='path to the test data, can be image path')
    parser.add_argument('-s', '--savefolder', default='TestSamples/examples/results', type=str,
                        help='path to the output directory, where results(obj, txt files) will be stored.')
    parser.add_argument('--device', default='cuda', type=str,
                        help='set device, cpu for using cpu')
    parser.add_argument('--useTex', default=False, type=lambda x: x.lower() in ['true', '1'],
                        help='whether to use FLAME texture model to generate uv texture map')
    parser.add_argument('--extractTex', default=True, type=lambda x: x.lower() in ['true', '1'],
                        help='whether to extract texture from input image as the uv texture map')
    parser.add_argument('--render_orig', default=True, type=lambda x: x.lower() in ['true', '1'],
                        help='whether to render results in original image size')
    parser.add_argument('--rasterizer_type', default='standard', type=str,
                        help='rasterizer type: pytorch3d or standard')

    args = parser.parse_args()
    process_image(args.inputpath, args.savefolder, args.device, args.useTex, args.rasterizer_type, args.extractTex, args.render_orig)
