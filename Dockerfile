FROM quay.io/jupyter/scipy-notebook:2024-02-24

USER root

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

RUN sudo -S \
apt-get update && apt-get install -y \
make \
gdebi

ARG QUARTO_VERSION="1.4.537"
RUN curl -o quarto-linux-arm64.deb -L https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-arm64.deb
RUN gdebi --non-interactive quarto-linux-arm64.deb




