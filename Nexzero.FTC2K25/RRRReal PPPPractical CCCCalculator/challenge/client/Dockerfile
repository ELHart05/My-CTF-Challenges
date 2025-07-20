FROM python:3.12-slim

WORKDIR /challenge

COPY . .

RUN rm -rf /challenge/server/ /challenge/.env

RUN pip install flask flask_limiter dotenv grpcio grpcio-tools

EXPOSE 4444

CMD ["python3", "client/app.py"]
