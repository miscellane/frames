# Image
FROM nvidia/cuda:12.2.0-base-ubuntu22.04


# Environment
SHELL [ "/bin/bash", "-c" ]


# Variables
ENV PYTHON_VIRTUAL_ENV=/opt/env


# Set application directory <app>
WORKDIR /mathematics


# Updates, additional packages, etc.
RUN  apt update && apt -q -y upgrade && apt -y install sudo && apt -y install vim && apt -y install wget && \
     apt -y install software-properties-common && add-apt-repository ppa:git-core/ppa && apt -y install git-all && \
     apt install -y build-essential libssl-dev libffi-dev && \
     apt install -y python3 python3-dev python3-pip python3-yaml python3-venv && \
     python3 -m venv $PYTHON_VIRTUAL_ENV
ENV PATH="$PYTHON_VIRTUAL_ENV/bin:$PATH"


# This command copies requirements.txt into /app
COPY ./requirements.txt .


# Virtual Environment
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade "jax[cuda12_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html && \
    python3 -m pip install --no-cache -r requirements.txt


# Hence
CMD ["/bin/bash"]