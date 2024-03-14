FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y procps

WORKDIR /raw/scrapers

COPY requirements.txt /raw/scrapers
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /raw/scrapers

CMD ["tail", "-f", "/dev/null"]
