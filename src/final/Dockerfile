FROM python:3.11.0b5-bullseye

#copy files
RUN mkdir /wu
COPY wu/ /wu
COPY requirements.txt requirements.txt

#install dependencies
RUN apt update && apt install -y python3-pip
RUN python3 -m pip install -r requirements.txt

#arguments
ARG consKey=nodefault
ARG consSec=nodefault
ARG accToken=nodefault
ARG accTokenSec=nodefault

#change stuff using args
RUN sed -i "s/conskey/${consKey}/" /wu/wu/.env
RUN sed -i "s/conssec/${consSec}/" /wu/wu/.env
RUN sed -i "s/acctoken/${accToken}/" /wu/wu/.env
RUN sed -i "s/acctoksec/${accTokenSec}/" /wu/wu/.env

EXPOSE 80
ENTRYPOINT python3 /wu/manage.py runserver 0.0.0.0:80