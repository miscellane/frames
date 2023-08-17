
<br>

## Notes


* [Docker](#docker)
* [JupyterLab & Docker](#jupyterlab--docker)
  * [Explore](#explore)
* [References](#references)

<br>

### Docker

The directory [registry](./registry/) lists a number of docker files, alongside supplements; in continuous development.


<br>
<br>


### JupyterLab & Docker

An [interesting article](https://www.docker.com/blog/supercharging-ai-ml-development-with-jupyterlab-and-docker/).  One of its key examples is

> docker container run <a href="https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the" title="remove">--rm</a> <a href="https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di" title="--interactive">-i</a> <a href="https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your" title="tag">-t</a> <a href="https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s" title="--publish">-p</a> 10000:8888 jupyter/base-notebook

wherein &nbsp; $-p \:\: 10000:8888$ &nbsp; maps the host port $10000$ to container port $8888$.


<br>

#### Explore


In brief, base image exploration is via

```bash
docker run --rm -i -t -p 10000:8888 jupyter/base-notebook
```

Extend the base image via [Dockerfile](./Dockerfile), and the command

```bash
docker build -t notebook .
```

Subsequently, a container/instance of the image `notebook` may be used as a development environment via the commands

```bash
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src="$(pwd)",target=/app notebook
```

or

```bash
docker run -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src="$(pwd)",target=/app notebook
```

Note, the container's working environment, i.e., `-w`, must be inline with this project's top directory.

<br>
<br>


### References

*  <a href="https://docs.nvidia.com/cuda/wsl-user-guide/index.html#nvidia-compute-software-support-on-wsl-2">NVIDIA Compute Software Support on Windows Subsystem for Linux (WSL) 2</a>
* [Docker & NVIDIA](https://docs.nvidia.com/ai-enterprise/deployment-guide-vmware/0.1.0/docker.html)
* [`conda`](https://docs.conda.io/en/latest/)
* [docker hub](https://hub.docker.com)
* [Python Package Index](https://pypi.org)
* [`pip`](https://pip.pypa.io/en/stable/)
  * [requirements file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/#requirements-file-format)
* `jax`
  * [python package index notes](https://pypi.org/project/jax/)
  * [GitHub](https://github.com/google/jax)
  * [Documentation](https://jax.readthedocs.io/en/latest/)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>