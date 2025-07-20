FROM python:3.12-slim

WORKDIR /challenge

COPY . .
RUN rm -rf /challenge/client/ /challenge/.env
RUN mv server/flag.txt /flag.txt

RUN pip install grpcio grpcio-tools

EXPOSE 8888

CMD ["python3", "server/server.py"]
