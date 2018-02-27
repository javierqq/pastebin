FROM python:3.6.1-alpine

RUN mkdir /code
WORKDIR /code
EXPOSE 80

ADD requirements.txt /code
RUN pip install -r requirements.txt
ADD . /code/

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "-h", "0.0.0.0", "-p", "80"]
