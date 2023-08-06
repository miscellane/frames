# Ubuntu
FROM ubuntu:lunar

# Update & Upgrade
RUN  apt update && apt -q -y upgrade && apt -y install sudo && apt -y install vim && apt -y install wget && \
     apt -y install software-properties-common && add-apt-repository ppa:git-core/ppa && apt -y install git-all && \
     apt install -y build-essential libssl-dev libffi-dev && \
     apt install -y python3 python3-dev python3-pip python3-yaml python3-venv

# Directory
WORKDIR /app

# Virtual Environment
# python3 -m venv env && source env/bin/activate

# Finally
CMD [ "/bin/bash" ]
