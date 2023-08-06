# Ubuntu
FROM ubuntu:lunar


# Environment
SHELL [ "/bin/bash", "-c" ]


# Update & Upgrade
RUN  apt update && apt -q -y upgrade && apt -y install sudo && apt -y install vim && apt -y install wget && \
     apt -y install software-properties-common && add-apt-repository ppa:git-core/ppa && apt -y install git-all && \
     apt install -y build-essential libssl-dev libffi-dev && \
     apt install -y python3 python3-dev python3-pip python3-yaml python3-venv


# Add a user


# Set application directory <app>
WORKDIR /app


# This command copies requirements.txt into /app
COPY ./requirements.txt .


# Virtual Environment
RUN python3 -m venv env && source env/bin/activate && python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade "jax[cuda12_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html && \
    python3 -m pip install --no-cache -r requirements.txt


# Finally
CMD [ "/bin/bash" ]
