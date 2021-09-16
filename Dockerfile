FROM python:3.8
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt && apt-get update && apt-get install python3-pip -y
EXPOSE 5000
CMD python3 app.py
