# Starting with a baseline NVIDIA/CUDA image
FROM nvidia/cuda:12.2.0-base-ubuntu20.04

# Path
ENV PATH=/opt/conda/bin:$PATH

# Environment
SHELL [ "/bin/bash", "-c" ]

# Ubuntu ...
RUN apt update && apt -q -y upgrade && apt -y install sudo && apt -y install vim && apt -y install wget

# From existing image ...
COPY --from=continuumio/miniconda3 /opt/conda /opt/conda

RUN conda init bash
SHELL [ "/bin/bash", "c"]

# Finally
CMD [ "/bin/bash" ]