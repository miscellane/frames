# Starting with a baseline NVIDIA/CUDA image
FROM nvidia/cuda:12.2.0-base-ubuntu20.04


# Variables
ENV PYTHON_PATH=/opt/miniconda3
ENV PYTHON_VIRTUAL_ENV=${PYTHON_PATH}/envs/tensors


# Command ...
SHELL [ "/bin/bash", "-c" ]


# Enhancing ...
RUN  apt update && apt -q -y upgrade && apt -y install sudo && apt -y install vim && apt -y install wget && \
     apt -y install software-properties-common && add-apt-repository ppa:git-core/ppa && apt -y install git-all && \
     wget -P Downloads https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh && \
     chmod +x Downloads/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh && \
     bash Downloads/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh -b -p ${PYTHON_PATH} && \
     conda init bash && conda config --set auto_activate_base false && \
     conda env create -f environment.yml -p $PYTHON_VIRTUAL_ENV
ENV PATH="$PYTHON_VIRTUAL_ENV/bin:$PATH"


# Hence
CMD [ "/bin/bash"]
