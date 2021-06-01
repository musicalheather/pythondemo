FROM python:3.7

COPY . /app
WORKDIR /app

RUN apt update
RUN pip3 install -r requirements.txt

EXPOSE 8080
RUN chmod +x start.sh
CMD ["/app/start.sh"]