FROM python:stretch

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN mkdir /usr/src/url-shortener-python

WORKDIR /usr/src/url-shortener-python

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"] 