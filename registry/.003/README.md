<br>

**JAX & Docker**

<br>

### Notes

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

<br>

Beaware of the effect of `apt -q -y upgrade`.

<br>
<br>

### References

* [PyMC](https://www.pymc.io/welcome.html)
  * [PyMC PyPI Page](https://pypi.org/project/pymc/): PyMC installs `arviz`
  * [Installing JAX](https://github.com/google/jax#installation): Installs `jax` & `jaxlib`
  * [PyMC installation notes vis-à-vis GPU (graphics processing units)](https://www.pymc-labs.io/blog-posts/pymc-stan-benchmark/#:~:text=worked%20for%20me%3A-,Install,-PyMC%20v4%20following)
* [Benchmarking Example](https://www.pymc-labs.io/blog-posts/pymc-stan-benchmark/)
* [Setting Up Python Environments](https://pythonspeed.com/articles/activate-virtualenv-dockerfile/)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>