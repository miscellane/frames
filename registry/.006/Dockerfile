# Starting with a baseline NVIDIA/CUDA image
FROM nvidia/cuda:12.2.0-base-ubuntu20.04


# From existing image ...
COPY --from=continuumio/miniconda3 /opt/conda /opt/conda

WORKDIR /app
COPY ./environment.yml .


# Path
ENV PATH=/opt/conda/bin:$PATH


# Environment
SHELL [ "/bin/bash", "-c" ]


# Ubuntu ...
RUN  apt update && apt -q -y upgrade && apt -y install sudo && apt -y install vim && apt -y install wget && \
  apt -y install software-properties-common && add-apt-repository ppa:git-core/ppa && apt -y install git-all && \
  conda init bash && conda config --set auto_activate_base true && conda env update -n base -f environment.yml && \
  echo -e 'export PATH="/opt/conda/bin:$PATH"\n\n' >> /etc/profile && \
  mkdir -p $CONDA_PREFIX/etc/conda/activate.d && \
  echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh && \
  echo 'export LD_LIBRARY_PATH=$CONDA_PREFIX/lib/:$CUDNN_PATH/lib:$LD_LIBRARY_PATH' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh && \
  useradd -ms /bin/bash algebra && usermod -aG sudo algebra


# Restarting
SHELL [ "/bin/bash", "-c"]


# Hence, the default user is
USER algebra


# ...
CMD [ "/bin/bash" ]
