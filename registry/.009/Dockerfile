# Image
FROM nvidia/cuda:12.2.0-base-ubuntu22.04


# Environment
SHELL [ "/bin/bash", "-c" ]


# Variables
ENV PYTHON_VIRTUAL_ENV=/opt/env


# Set application directory <app>
WORKDIR /app


# This command copies requirements.txt into /app
COPY ./requirements.txt ./cudnn-linux-x86_64-8.9.3.28_cuda12-archive.tar.xz /app/


# Updates, additional packages, etc.
# Live, temporary, current session -> export PATH="$PYTHON_VIRTUAL_ENV/bin:$PATH"
# Upcoming
#   https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local
#   https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#download
RUN apt update && apt -q -y upgrade && apt -y install sudo && apt -y install vim && apt -y install wget && \
    apt -y install software-properties-common && add-apt-repository ppa:git-core/ppa && apt -y install git-all && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin && \
    sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600 && \
    wget https://developer.download.nvidia.com/compute/cuda/12.2.1/local_installers/cuda-repo-wsl-ubuntu-12-2-local_12.2.1-1_amd64.deb && \
    sudo dpkg -i cuda-repo-wsl-ubuntu-12-2-local_12.2.1-1_amd64.deb && \
    sudo cp /var/cuda-repo-wsl-ubuntu-12-2-local/cuda-*-keyring.gpg /usr/share/keyrings/ && \
    sudo apt update && \
    sudo apt -y install cuda && \
    tar -xvf cudnn-linux-x86_64-8.9.3.28_cuda12-archive.tar.xz && \
    sudo cp cudnn-linux-x86_64-8.9.3.28_cuda12-archive/include/cudnn*.h /usr/local/cuda/include && \
    sudo cp -P cudnn-linux-x86_64-8.9.3.28_cuda12-archive/lib/libcudnn* /usr/local/cuda/lib64 && \
    sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn* && \
    apt install -y build-essential libssl-dev libffi-dev && \
    apt install -y python3 python3-dev python3-pip python3-yaml python3-venv && \
    python3 -m venv $PYTHON_VIRTUAL_ENV
ENV PATH="$PYTHON_VIRTUAL_ENV/bin:$PATH"


# Virtual Environment
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade "jax[cuda12_local]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html && \
    python3 -m pip install --no-cache -r requirements.txt


# Hence
CMD ["/bin/bash"]