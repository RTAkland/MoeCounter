FROM ubuntu:latest
EXPOSE 8000
WORKDIR .
COPY . .
RUN apt-get -y update && apt-get -y install python3-pip && pip3 install -r requirements.txt
CMD ["python3", "main.py"]