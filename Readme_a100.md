### container

docker run --gpus all -it --rm -v /data/sunlf:/workspace/project -p 8501:8501 nvcr.io/nvidia/pytorch:23.04-py3


docker run --gpus all -it --rm -v /data/sunlf:/workspace/project -p 8502:8502 sunlf:latest
#### run fetch 

```
chmod +x fetch_data.sh
./fetch_data.sh
```

#### build pytorch3d

```
git clone https://github.com/facebookresearch/pytorch3d.git
cd pytorch3d && pip install -e .
```

result is 

```
Looking in indexes: https://pypi.org/simple, https://pypi.ngc.nvidia.com
Obtaining file:///workspace/project/pytorch3d
Collecting iopath
  Downloading iopath-0.1.10.tar.gz (42 kB)
     |████████████████████████████████| 42 kB 792 kB/s 
Requirement already satisfied: tqdm in /usr/local/lib/python3.8/dist-packages (from iopath->pytorch3d==0.7.7) (4.65.0)
Requirement already satisfied: typing_extensions in /usr/local/lib/python3.8/dist-packages (from iopath->pytorch3d==0.7.7) (4.5.0)
Collecting portalocker
  Downloading portalocker-2.10.1-py3-none-any.whl (18 kB)
Building wheels for collected packages: iopath
  Building wheel for iopath (setup.py) ... done
  Created wheel for iopath: filename=iopath-0.1.10-py3-none-any.whl size=31547 sha256=991625823cbbcb3a57017bdf7e6edc8be04e189339d68bce4ab5e0fbaea485b6
  Stored in directory: /tmp/pip-ephem-wheel-cache-pcpwhlxd/wheels/89/3e/24/0f349c0b2eeb6965903035f3b00dbb5c9bea437b4a2f18d82c
Successfully built iopath
Installing collected packages: portalocker, iopath, pytorch3d
  Running setup.py develop for pytorch3d
Successfully installed iopath-0.1.10 portalocker-2.10.1 pytorch3d-0.7.7
```

#### another method

```
python setup.py bdist_wheel
```

```
pip install pytorch3d-0.7.7-cp38-cp38-linux_aarch64.whl
```

### pip install

```
pip install -r requirement_a100.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### run script

```
python demos/demo_reconstruct.py -i TestSamples/examples --saveDepth True --saveObj True --rasterizer_type=pytorch3d 
```

### doc 

```
https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/rel-23-04.html

https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch

```


### run flask

```
```

#### run test

```
curl -X POST "http://localhost:5000/process-image" -F "file=@/workspace/project/DECA/TestSamples/AFLW2000/image00181.jpg"

```

### cuda info in container

```
root@4fd171ebb889:/workspace# nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Tue_Feb__7_19:32:53_PST_2023
Cuda compilation tools, release 12.1, V12.1.66
Build cuda_12.1.r12.1/compiler.32415258_0
root@4fd171ebb889:/workspace# nvidia-smi
Sun Sep  8 23:22:59 2024       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.28.03              Driver Version: 560.28.03      CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A100-PCIE-40GB          Off |   00000000:01:00.0 Off |                    0 |
| N/A   31C    P0             36W /  250W |       4MiB /  40960MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA A100-PCIE-40GB          Off |   00000000:02:00.0 Off |                    0 |
| N/A   31C    P0             36W /  250W |       4MiB /  40960MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA A100-PCIE-40GB          Off |   00000000:81:00.0 Off |                    0 |
| N/A   31C    P0             37W /  250W |       4MiB /  40960MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA A100-PCIE-40GB          Off |   00000000:82:00.0 Off |                    0 |
| N/A   31C    P0             37W /  250W |       4MiB /  40960MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

```
