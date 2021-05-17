FROM python:3.6

COPY . /app
WORKDIR /app

RUN apt update && apt install -y postgresql-client
RUN pip3 install -r requirements.txt

CMD chmod +x start.sh && ./start.sh