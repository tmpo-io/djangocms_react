FROM python:2.7-alpine3.8

WORKDIR /app

RUN apk --no-cache add \
  build-base \
  cairo-dev \
  gdk-pixbuf-dev \
  jpeg-dev \
  libffi-dev \
  libxml2-dev \
  libxslt-dev \
  mariadb-dev \
  pango-dev \
  zlib-dev

RUN pip install --upgrade pip

RUN pip install gunicorn

COPY src/requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "{{ cookiecutter.project_name }}.wsgi", "-b", "0.0.0.0:8000", "-w", "1"]
