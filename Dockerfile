FROM quay.io/jupyter/r-notebook:2023-11-19

USER root

RUN conda install matplotlib=3.8.3 -y
RUN conda install numpy=1.26.4 -y
RUN conda install pandas=2.2.1 -y
RUN conda install scikit-learn=1.4.1.post1 -y
RUN conda install seaborn=0.13.2 -y
# RUN conda install conda-forge::altair=5.2.0 -y
RUN conda install click=8.1.7 -y
RUN conda install altair=5.2.0 -y
RUN conda install quarto=1.3.450 -y
RUN conda install tabulate=0.9.0 -y


RUN apt-get update 
RUN apt-get install fonts-lmodern -y 
RUN apt-get install lmodern -y



