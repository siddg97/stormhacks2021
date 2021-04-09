FROM node:alpine as base
ENV CI=true
WORKDIR /app
COPY package.json .
RUN yarn install
COPY . .
CMD ["yarn", "start"]