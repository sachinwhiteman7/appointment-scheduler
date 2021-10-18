FROM python:3.8

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# Install postgres client

RUN apt-get -y update
RUN apt-get install -y python
# Install individual dependencies
# so that we could avoid installing extra packages to the container
# RUN apt-get install --update --no-cache --virtual .tmp-build-deps \
# 	gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt

# Remove dependencies
RUN apt-get -y update && apt-get -y autoremove

RUN mkdir /app
WORKDIR /app

# entrypoint, must be executable file chmod +x entrypoint.sh
COPY entrypoint.sh /app/entrypoint.sh

# what happens when I start the container
CMD ["/app/entrypoint.sh"]