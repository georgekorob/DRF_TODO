from python:3.7.0

RUN apt-get update \
&& apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip

COPY ./ ./
RUN pip3 install -r requirements.txt
RUN pip3 install psycopg2-binary==2.9.3
RUN pip3 install gunicorn
