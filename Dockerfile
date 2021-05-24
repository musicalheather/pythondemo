FROM python:3.7

COPY . /app
WORKDIR /app

RUN apt update && apt install -y postgresql-client
RUN pip3 install -r requirements.txt

RUN chmod +x start.sh
CMD ["/app/start.sh"]