FROM python:3.7-slim-buster

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove

COPY ./requirements.txt /thrive-market/requirements.txt
WORKDIR /thrive-market
RUN pip install -r requirements.txt

COPY . /thrive-market

ENV FLASK_APP=server.py
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
