FROM node:alpine

WORKDIR /app

COPY ./ /app

RUN yarn config set registry https://registry.npm.taobao.org/ && yarn

CMD ["npm", "start"]
