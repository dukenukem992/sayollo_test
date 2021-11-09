FROM python:3.8
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
WORKDIR /app
COPY . /app
CMD ["uvicorn", "app:api", "--reload", "--host", "0.0.0.0", "--port", "5000"]
