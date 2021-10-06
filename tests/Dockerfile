FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install fastapi && pip3 install requests
ADD authentification.py /tests/authentification.py
WORKDIR /app/tests
CMD python3 /tests/authentification.py

