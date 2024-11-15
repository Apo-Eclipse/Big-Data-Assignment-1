FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip 
RUN pip3 install --break-system-packages  pandas numpy seaborn matplotlib scikit-learn scipy 
RUN mkdir -p /home/doc-bd-a1

COPY dataset.csv /home/doc-bd-a1/
COPY load.py /home/doc-bd-a1/
COPY dpre.py /home/doc-bd-a1/
COPY eda.py /home/doc-bd-a1/
COPY model.py /home/doc-bd-a1/
COPY vis.py /home/doc-bd-a1/

WORKDIR /home/doc-bd-a1
CMD ["bash"]