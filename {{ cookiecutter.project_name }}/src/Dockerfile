FROM python:2.7
RUN pip install --upgrade pip
RUN pip install gunicorn
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app

CMD ["gunicorn", "{{ cookiecutter.project_name }}.wsgi", "-b", "0.0.0.0:8000", "-w", "1"]

EXPOSE 8000
