# Starting with ...
FROM greyhypotheses/jax


# Set working directory
WORKDIR /app


# This command copies requirements.txt into /app
COPY ./requirements.txt .


# Updating the packages of the underlying operating system, and addressing privileges
# ... apt install nvidia-modprobe
# ... privileges -> https://linux.die.net/man/8/chpasswd
# Note:
# --no-cache => do not save downloads
#
RUN apt update && python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache -r requirements.txt && \
    useradd -m algebra && echo "algebra:algebra" | chpasswd && \
    adduser algebra sudo


# Hence, setting the default user ...
USER algebra


# Finally
CMD [ "/bin/bash" ]
