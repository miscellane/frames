# Starting with a baseline NVIDIA/CUDA image
FROM nvidia/cuda:12.2.0-base-ubuntu20.04

# Path
ENV PATH=/opt/conda/bin:$PATH

# Environment
SHELL [ "/bin/bash", "-c" ]

# Ubuntu ...
RUN  apt update && apt -q -y upgrade && apt -y install sudo && apt -y install vim && apt -y install wget && \ 
  apt -y install software-properties-common && add-apt-repository ppa:git-core/ppa && apt -y install git-all

# From existing image ...
COPY --from=continuumio/miniconda3 /opt/conda /opt/conda
RUN conda init bash && conda config --set auto_activate_base false
SHELL [ "/bin/bash", "-c"]

# mkdir -p $CONDA_PREFIX/etc/conda/activate.d
# echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
# echo 'export LD_LIBRARY_PATH=$CONDA_PREFIX/lib/:$CUDNN_PATH/lib:$LD_LIBRARY_PATH' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

# Evaluating ...
RUN useradd -m algebra && usermod -aG sudo algebra

# Hence, the default user is
USER algebra

# Set application directory <app>
WORKDIR /app

# This command copies requirements.txt into /app
# COPY ./requirements.txt .

# --no-cache => do not save downloads
# RUN python -m pip install --no-cache -r requirements.txt

# ...
CMD [ "/bin/bash" ]
