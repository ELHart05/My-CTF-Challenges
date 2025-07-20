FROM node:20-buster-slim

RUN apt-get update \
    && apt-get install -y python3 build-essential \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./challenge/package.json ./challenge/package-lock.json ./
RUN npm i

COPY ./challenge/public ./public
COPY ./challenge/app.js .

CMD ["npm", "start"]