FROM node:alpine

WORKDIR /app

COPY src /app

RUN yarn config set registry https://registry.npm.taobao.org/ && yarn

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
