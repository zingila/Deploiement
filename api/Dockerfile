FROM python:3.9-slim

COPY requirements.txt /api/requirements.txt
RUN pip3 install -r /api/requirements.txt

EXPOSE 8000

COPY . .

CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000"]
