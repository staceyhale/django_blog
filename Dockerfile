FROM python:3.11

ENV PYTHONDONTWRITTEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /django_blog

COPY . .

RUN apt update -y \
    && apt upgrade -y \
    && apt install -y gettext \
    && python -m pip install --upgrade pip \
	&& pip install -r requirements.txt \
	&& pip install gunicorn

RUN useradd -m -s /bin/bash stacy

RUN chown -R stacy:stacy /django_blog

USER stacy

