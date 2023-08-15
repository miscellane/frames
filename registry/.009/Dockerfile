# Image
FROM nvidia/cuda:12.2.0-base-ubuntu22.04


# Environment
SHELL [ "/bin/bash", "-c" ]


# Variables
ENV PYTHON_VIRTUAL_ENV=/opt/env


# Set application directory <app>
WORKDIR /app


# This command copies requirements.txt into /app
COPY ./.009/requirements.txt ./cudnn-linux-x86_64-8.9.3.28_cuda12-archive.tar.xz /app/


# Updates, additional packages, etc.
RUN apt update && apt -y install sudo && apt -y install vim && apt -y install wget && \
    apt -y install software-properties-common && add-apt-repository ppa:git-core/ppa && apt -y install git-all && \
    apt install -y build-essential libssl-dev libffi-dev && \
    apt install -y python3 python3-dev python3-pip python3-yaml python3-venv && \
    python3 -m venv $PYTHON_VIRTUAL_ENV && \
    source ${PYTHON_VIRTUAL_ENV}/bin/activate && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache -r requirements.txt
ENV PATH="$PYTHON_VIRTUAL_ENV/bin:$PATH"


# Hence
CMD ["/bin/bash"]