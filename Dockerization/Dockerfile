FROM python:latest

LABEL description = "fastapi and sqlite image"

ENV FASTAPI_PORT = 8000

COPY ./requirements.txt ./

RUN pip install -r requirements.txt && apt-get update && apt-get install -y sqlite3

COPY ./data-saving-app /opt/source-code

WORKDIR /opt/source-code

CMD uvicorn app:app --host=0.0.0.0 --port=8000 --reload
