FROM quay.io/jupyter/scipy-notebook:2024-02-24

USER root

RUN conda install -y matplotlib=3.8.3 \
numpy=1.26.4 \
pandas=2.2.1 \
scikit-learn=1.4.1.post1 \
seaborn=0.13.2 \
click=8.1.7 \
quarto=1.4.550  \
tabulate=0.9.0 

RUN pip install renewenergy==0.1.0

RUN conda install conda-forge::altair=5.2.0 -y

RUN apt-get update 
RUN apt-get install fonts-lmodern -y 
RUN apt-get install lmodern -y 
