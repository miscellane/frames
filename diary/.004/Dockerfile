# Starting with ...
FROM baseImage

# A user
RUN useradd -m algebra && usermod -aG sudo algebra

# Hence, the default user is
USER algebra

# Working directory
WORKDIR /app

# Hence
CMD [ "/bin/bash"]