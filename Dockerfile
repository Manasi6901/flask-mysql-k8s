FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask mysql-connector-python
CMD ["python", "app.py"]

