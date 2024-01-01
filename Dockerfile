FROM python:3.9.18-slim
WORKDIR /home
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git
RUN git clone https://github.com/lugonesnicolas/scrap_in_docker_container.git
WORKDIR /home/scrap_in_docker_container
COPY . .
RUN git pull origin main
RUN pip install -r requirements.txt
RUN git config --global user.email lugones.nicolas@gmail.com
RUN git config --global user.name lugonesnicolas
RUN git remote set-url origin https://lugonesnicolas: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@github.com/lugonesnicolas/scrap_in_docker_container
RUN echo "venv/" > .gitignore
RUN python3 main.py
RUN rm -r .gitignore
RUN git add guia.txt
RUN git add .
RUN git commit -m "Nuevo tocken"
RUN git push origin main
COPY . .