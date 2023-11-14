FROM python:3.10-alpine

COPY --chown=keycraft:keycraft . /app
WORKDIR /app

RUN pip install .

RUN adduser -D keycraft
USER keycraft

ENTRYPOINT ["keycraft"]
