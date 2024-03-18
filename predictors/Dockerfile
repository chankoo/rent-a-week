FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y procps

WORKDIR /raw/predictors

COPY requirements.txt /raw/predictors
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /raw/predictors

CMD ["tail", "-f", "/dev/null"]
