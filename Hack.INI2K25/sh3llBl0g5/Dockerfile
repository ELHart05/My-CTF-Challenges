FROM node:14 AS build

WORKDIR /app
COPY ./challenge/package*.json ./
RUN npm install
COPY ./challenge .

ARG VUE_APP_AKEY
ARG VUE_APP_ADOMAIN
ARG VUE_APP_PID
ARG VUE_APP_SBUCKET
ARG VUE_APP_MSID
ARG VUE_APP_AID

RUN echo "VUE_APP_AKEY=$VUE_APP_AKEY" > .env && \
    echo "VUE_APP_ADOMAIN=$VUE_APP_ADOMAIN" >> .env && \
    echo "VUE_APP_PID=$VUE_APP_PID" >> .env && \
    echo "VUE_APP_SBUCKET=$VUE_APP_SBUCKET" >> .env && \
    echo "VUE_APP_MSID=$VUE_APP_MSID" >> .env && \
    echo "VUE_APP_AID=$VUE_APP_AID" >> .env

RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY ./config/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]