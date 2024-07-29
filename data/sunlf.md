## cuda command

### ubuntu 

18.04

### nvidia-smi

```bash

Fri Jul 26 20:32:16 2024       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 530.30.02              Driver Version: 530.30.02    CUDA Version: 12.1     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                  Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf            Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3090         On | 00000000:AF:00.0 Off |                  N/A |
| 30%   39C    P8               24W / 350W|    643MiB / 24576MiB |      5%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A      1533      G   /usr/lib/xorg/Xorg                           18MiB |
|    0   N/A  N/A      1613      G   /usr/bin/gnome-shell                         72MiB |
|    0   N/A  N/A      1953      G   /usr/lib/xorg/Xorg                          298MiB |
|    0   N/A  N/A      2099      G   /usr/bin/gnome-shell                         69MiB |
|    0   N/A  N/A      2353      G   ...in/bin/sunloginclient --cmd=autorun       19MiB |
|    0   N/A  N/A      2394      G   ...) Chrome/58.0.3029.81 Safari/537.36        4MiB |
|    0   N/A  N/A      2420      G   ...en=2DDDB722D755788D97708A09E2D84612        7MiB |
|    0   N/A  N/A      2842      G   ...erProcess --variations-seed-version      148MiB |
+---------------------------------------------------------------------------------------+

```


### nvcc --version

```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2020 NVIDIA Corporation
Built on Mon_Oct_12_20:09:46_PDT_2020
Cuda compilation tools, release 11.1, V11.1.105
Build cuda_11.1.TC455_06.29190527_0
```


### doc

https://doi.org/10.1016/j.cad.2021.103084
https://doi.org/10.1145/1778765.1778855
https://doi.org/10.1111/j.1467-8659.2009.01610.x