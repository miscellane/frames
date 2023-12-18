# Starting with ...
FROM continuumio/miniconda3

# The .yml
WORKDIR /app

COPY ./environment.yml .

RUN conda init bash && conda config --set auto_activate_base false && \
    conda env create -f environment.yml -p /opt/conda/envs/transcribe && \
    echo "source activate transcribe" > ~/.bashrc

# Virtual Environment
ENV PYTHON_VIRTUAL_ENV=/opt/conda/envs/transcribe


# Path
ENV PATH=${PYTHON_VIRTUAL_ENV}/bin:$PATH


# Restarting ...
SHELL ["/bin/bash", "-c"]