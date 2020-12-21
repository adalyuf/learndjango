FROM python:3
ENV PYTHONBUFFERED=1
WORKDIR /app/
COPY . /app/
RUN pip install -r requirements.txt
