# Starting with a baseline NVIDIA/CUDA image
FROM nvidia/cuda:12.2.0-base-ubuntu20.04


# From existing image ...
COPY --from=continuumio/miniconda3 /opt/conda /opt/conda
ENV PATH=/opt/conda/bin:$PATH


# The .yml
WORKDIR /app
COPY ./environment.yml .


# Environment
SHELL [ "/bin/bash", "-c" ]


# Update & Upgrade
RUN  apt update && apt -q -y upgrade && apt -y install sudo && apt -y install vim && apt -y install wget && \
  apt -y install software-properties-common && add-apt-repository ppa:git-core/ppa && apt -y install git-all && \
  conda init bash && conda config --set auto_activate_base false && \
  conda env create --solver libmamba -f environment.yml -p /opt/conda/envs/networks && \
  echo "conda activate networks" >> ~/.bashrc


# Virtual Environment
ENV PYTHON_VIRTUAL_ENV=/opt/conda/envs/networks


# Path
ENV PATH=${PYTHON_VIRTUAL_ENV}/bin:$PATH


# Restarting ...
SHELL [ "/bin/bash", "-c"]
