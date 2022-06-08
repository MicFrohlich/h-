FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
COPY ./start.sh .
COPY ./requirements.txt /requirements.txt
COPY ./app.py . 
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
WORKDIR /app

EXPOSE 5000