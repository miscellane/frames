# Starting with a baseline NVIDIA/CUDA image
FROM nvidia/cuda:12.2.0-base-ubuntu20.04

# Identifier
RUN IDENTIFIER=$(cat /proc/1/cpuset | cut -c9-)

# From existing image ...
COPY --from=continuumio/miniconda3 /opt/conda /opt/conda

# Path
ENV PATH=/opt/conda/bin:$PATH

SHELL [ "/bin/bash"]

# Finally
CMD [ "/bin/bash" ]