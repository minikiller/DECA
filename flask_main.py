from flask import Flask, request, jsonify, send_file
from PIL import Image
import io
import os
import cv2
import numpy as np
from scipy.io import savemat
import torch
from decalib.deca import DECA
from decalib.datasets import datasets 
from decalib.utils import util
from decalib.utils.config import cfg as deca_cfg
from decalib.utils.tensor_cropper import transform_points

app = Flask(__name__)

# 配置 DECA 模型
device = 'cuda' if torch.cuda.is_available() else 'cpu'
deca_cfg.model.use_tex = False
# deca_cfg.rasterizer_type = 'standard'
deca_cfg.rasterizer_type = 'pytorch3d'   # 设置 rasterizer_type 为 pytorch3d
deca_cfg.save_obj=True
deca_cfg.model.extract_tex = True
deca = DECA(config=deca_cfg, device=device)

@app.route('/process-image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 读取图像
    img = Image.open(file.stream).convert('RGB')
    img_tensor = transform_points(img).to(device)  # 变换为模型需要的格式
    
    with torch.no_grad():
        codedict = deca.encode(img_tensor[None, ...])
        opdict, visdict = deca.decode(codedict)
        
        # 处理并保存结果
        depth_image = deca.render.render_depth(opdict['trans_verts']).repeat(1, 3, 1, 1)
        depth_img_io = io.BytesIO()
        depth_image_pil = util.tensor2image(depth_image[0])
        depth_image_pil.save(depth_img_io, 'JPEG')
        depth_img_io.seek(0)

        # 返回处理后的深度图像
        return send_file(depth_img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
