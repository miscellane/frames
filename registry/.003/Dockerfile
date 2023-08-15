# Starting with ...
FROM nvidia/cuda:12.2.0-base-ubuntu22.04


# From existing image ...
COPY --from=continuumio/miniconda3 /opt/conda /opt/conda


# The .yml
WORKDIR /app
COPY ./environment.yml .


# Environment
SHELL [ "/bin/bash", "-c" ]


# Update & Upgrade
RUN  apt -y update && apt -y install sudo && apt -y install vim && apt -y install wget && \
     apt -y install software-properties-common && add-apt-repository ppa:git-core/ppa && apt -y install git-all && \
     conda init bash && conda config --set auto_activate_base false && \
     conda env create -f environment.yml -p /opt/conda/envs/uncertainty && \
     echo "conda activate uncertainty" >> ~/.bashrc


# Virtual Environment
ENV PYTHON_VIRTUAL_ENV=/opt/conda/envs/uncertainty


# Path
ENV PATH=${PYTHON_VIRTUAL_ENV}/bin:$PATH


# Restarting ...
SHELL [ "/bin/bash", "-c"]
