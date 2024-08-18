# Use a slim base image with Python 3.11
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY run.py /app/run.py
CMD ["sh", "-c", "python3 /app/run.py"]
