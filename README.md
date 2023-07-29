
<br>

## Rough Notes

<br>

### Initially

Explore the base image

```bash
docker run --rm -i -t -p 10000:8888 jupyter/base-notebook
```

```bash
docker run --rm -i -t -p 10000:8888 -v ~/library/miscellane/frames jupyter/base-notebook
```

<br>

Extend the base image via a `Dockerfile` ...

```bash
docker build -t notebook .
```

```bash
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src="$(pwd)",target=/app notebook
```

```bash
docker run -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src="$(pwd)",target=/app notebook
```

<br>
<br>

### JupyterLab & Docker

An [interesting article](https://www.docker.com/blog/supercharging-ai-ml-development-with-jupyterlab-and-docker/).  One of its key examples is

> docker container run <a href="https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the" title="remove">--rm</a> <a href="https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di" title="--interactive">-i</a> <a href="https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your" title="tag">-t</a> <a href="https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s" title="--publish">-p</a> 10000:8888 jupyter/base-notebook

wherein `-p 10000:8888` maps the host port $10000$ to container port $8888$

<br>

Build a new container image using the Dockerfile in the current directory, i.e., the closing `.`; the image's tag is `notebook`.

> docker build -t notebook .


<br>
<br>

### References

*  <a href="https://docs.nvidia.com/cuda/wsl-user-guide/index.html#nvidia-compute-software-support-on-wsl-2">NVIDIA Compute Software Support on <abbr title="Windows Subsystem for Linux">WSL 2</abbr></a>
* [Docker & NVIDIA](https://docs.nvidia.com/ai-enterprise/deployment-guide-vmware/0.1.0/docker.html)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>