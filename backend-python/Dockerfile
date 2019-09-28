FROM python:3.7-alpine

WORKDIR /app

RUN pip install flask pymongo && \
    chmod 0500 /tmp

COPY ./src/app.py /app/app.py
COPY ./start.sh /start.sh
RUN chmod +x /start.sh

CMD [ "/start.sh"]
