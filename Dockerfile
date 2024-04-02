# FROM quay.io/jupyter/scipy-notebook:2024-02-24

FROM quay.io/jupyter/minimal-notebook:x86_64-ubuntu-22.04

USER root

RUN apt-get update

RUN apt-get install -y --no-install-recommends \
    pandoc \
    pandoc-citeproc \
    curl \
    gdebi-core \
    lmodern \
    && rm -rf /var/lib/apt/lists/*


RUN conda install conda
RUN conda install matplotlib=3.8.3 -y
RUN conda install numpy=1.26.4 -y
RUN conda install pandas=2.2.1 -y
RUN conda install scikit-learn=1.4.1.post1 -y
RUN conda install seaborn=0.13.2 -y
RUN conda install conda-forge::altair=5.2.0 -y
RUN conda install click=8.1.7 -y
# RUN conda install quarto=1.4.550 -y
RUN conda install tabulate=0.9.0 -y

RUN apt-get update 
RUN apt-get install fonts-lmodern -y 
RUN apt-get install lmodern -y 

RUN curl -LO https://quarto.org/download/latest/quarto-linux-amd64.deb
RUN gdebi --non-interactive quarto-linux-amd64.deb

# USER ${NB_UID} 
# ARG QUARTO_VERSION="1.4.550"
# RUN curl -o quarto-linux-amd64.deb -L https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.deb
# RUN gdebi --non-interactive quarto-linux-amd64.deb


# # And to install gdebi:
# USER root

# RUN sudo -S \
#     apt-get update && apt-get install -y \
#     make \
#     gdebi



