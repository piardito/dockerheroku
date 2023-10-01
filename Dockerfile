FROM python:3.10
COPY . /projetcredit
WORKDIR /projetcredit
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT projetcredit:app