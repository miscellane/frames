<br>

**JAX & Docker (cf. .003)**

<br>

How should a docker image for `PyMC` + GPU (Graphics Processing Units) be built?  It is quite probable that `jax[cuda12_pip]` addresses/delivers

```shell
RUN wget https://developer.download.nvidia.com/compute/cuda/12.2.1/local_installers/cuda_12.2.1_535.86.10_linux.run && \
    sudo sh cuda_12.2.1_535.86.10_linux.run && \
    tar -xvf cudnn-linux-x86_64-8.9.3.28_cuda12-archive.tar.xz && \
    sudo cp cudnn-linux-x86_64-8.9.3.28_cuda12-archive/include/cudnn*.h /usr/local/cuda/include && \
    sudo cp -P cudnn-linux-x86_64-8.9.3.28_cuda12-archive/lib/libcudnn* /usr/local/cuda/lib64 && \
    sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
```

The packages are from

* [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local)
* [cuDNN](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#download)

Rethink `apt -q -y upgrade`.

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>