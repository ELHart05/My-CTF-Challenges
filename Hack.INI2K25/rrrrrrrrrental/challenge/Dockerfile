FROM node:18-slim

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install --production

COPY . .

ENV SECRET_KEY=36d8b93ed19893592a0339fcd47d48d4dba9ff443eed174ab5f7805f729b2a29

EXPOSE 3000

CMD [ "npm", "start" ]
