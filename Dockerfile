FROM jupyter/base-notebook

# Delete the default application directory
RUN rm -rf /home/jovyan

# Set application directory <app>
WORKDIR /app

# This command copies requirements.txt into /app
COPY ./requirements.txt .

# --no-cache => do not save downloads
RUN python -m pip install --no-cache -r requirements.txt