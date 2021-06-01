FROM python:3.7

COPY . /app
WORKDIR /app

RUN apt update
RUN pip3 install -r requirements.txt

RUN chmod +x start.sh
CMD ["start.sh"]