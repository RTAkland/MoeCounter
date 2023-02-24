FROM ubuntu:latest
EXPOSE 8000
WORKDIR .
COPY . .
RUN apt-get -y update && apt-get -y install python3-pip && pip3 install -r requirements.txt
CMD ["uvicorn", "src:create_app", "--host=0.0.0.0", "--port=8000"]