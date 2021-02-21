FROM node:alpine
WORKDIR /app

COPY package.json .
COPY yarn.lock .

RUN yarn install --network-timeout 1000000

COPY . .
CMD [ "yarn", "start"]