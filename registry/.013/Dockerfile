# Starting with ...
FROM ubuntu:lunar


# The requirements
WORKDIR /app
COPY ./requirements.txt .


# Environment
SHELL [ "/bin/bash", "-c" ]


# Python Virtual Environment ...
ENV PYTHON_VIRTUAL_ENV=/opt/env


# Options
RUN  apt update && apt -q -y upgrade && apt -y install sudo && apt -y install vim && apt -y install wget && \
     apt -y install software-properties-common && add-apt-repository ppa:git-core/ppa && apt -y install git-all && \
     apt install -y build-essential libssl-dev libffi-dev && \
     apt install -y python3 python3-dev python3-pip python3-yaml python3-venv && \
     python3 -m venv $PYTHON_VIRTUAL_ENV
ENV PATH="${PYTHON_VIRTUAL_ENV}/bin:$PATH"


# Restarting ...
SHELL [ "/bin/bash", "-c" ]


# Hence ...
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache -r requirements.txt


