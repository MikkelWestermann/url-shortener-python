FROM python:stretch

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN mkdir /usr/src/url-shortener

WORKDIR /usr/src/url-shortener

COPY ./ ./

RUN pip install -r requirements.txt

ENTRYPOINT ["flask"]
CMD ["run"]