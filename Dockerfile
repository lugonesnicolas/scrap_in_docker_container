#Dockerfile, Image, Container
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python", "main.py"]