FROM debian:buster-slim
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y unixodbc-dev python3-dev g++ python3-pip libgssapi-krb5-2
COPY ./requirements.txt /usr/src/requirements.txt
RUN python3 -m pip install -r /usr/src/requirements.txt

COPY . /usr/src
WORKDIR /usr/src
# RUN python3 -m pytest /usr/src
EXPOSE 80
CMD ["uvicorn", "application.main:app", "--host", "0.0.0.0", "--port", "80"]