# Starting with a baseline NVIDIA/CUDA image
FROM nvidia/cuda:12.2.0-base-ubuntu20.04

# From existing image ...
COPY --from=continuumio/miniconda3 /opt/conda /opt/conda

# Path
ENV PATH=/opt/conda/bin:$PATH

# Environment
SHELL [ "/bin/bash", "-c" ]

# Ubuntu ...
RUN  apt update && apt -q -y upgrade && apt -y install sudo && apt -y install vim && apt -y install wget && \ 
  apt -y install software-properties-common && add-apt-repository ppa:git-core/ppa && apt -y install git-all && \ 
  conda init bash && conda config --set auto_activate_base false && conda create --prefix /opt/conda/envs/tensors

# Restarting ...
RUN echo "conda activate tensors" >> ~/.bashrc
SHELL [ "/bin/bash", "-c"]
