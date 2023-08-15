# Starting with ...
FROM baseImage


# Set working directory
WORKDIR /app


# This command copies requirements.txt into /app
COPY ./requirements.txt .


# Packages
RUN apt update && \
    python -m pip install --upgrade pip && \
    python -m pip install --no-cache -r requirements.txt


# Finally
CMD [ "/bin/bash" ]
