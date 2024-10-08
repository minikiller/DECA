### run command

```
nvidia-smi 
```
### result

```
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 530.30.02              Driver Version: 530.30.02    CUDA Version: 12.1     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                  Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf            Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3090         On | 00000000:AF:00.0 Off |                  N/A |
| 30%   35C    P8               24W / 350W|    579MiB / 24576MiB |      5%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A      1570      G   /usr/lib/xorg/Xorg                           18MiB |
|    0   N/A  N/A      1651      G   /usr/bin/gnome-shell                         72MiB |
|    0   N/A  N/A      2028      G   /usr/lib/xorg/Xorg                          296MiB |
|    0   N/A  N/A      2174      G   /usr/bin/gnome-shell                         60MiB |
|    0   N/A  N/A      2427      G   ...in/bin/sunloginclient --cmd=autorun       18MiB |
|    0   N/A  N/A      2458      G   ...) Chrome/58.0.3029.81 Safari/537.36        4MiB |
|    0   N/A  N/A      2487      G   ...en=8A55E589D27AAE58455F0E43AE267A70       11MiB |
|    0   N/A  N/A      3488      G   ...erProcess --variations-seed-version       90MiB |
+---------------------------------------------------------------------------------------+
```

```
nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Mon_Apr__3_17:16:06_PDT_2023
Cuda compilation tools, release 12.1, V12.1.105
Build cuda_12.1.r12.1/compiler.32688072_0 
```
