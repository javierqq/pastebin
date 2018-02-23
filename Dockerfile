FROM python:3.6.1-alpine

RUN mkdir /code
WORKDIR /code
EXPOSE 5000

ADD requirements.txt /code
RUN pip install -r requirements.txt
ADD . /code/

CMD ["python", "manage.py", "runserver", "-h", "0.0.0.0"]