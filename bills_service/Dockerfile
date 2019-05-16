FROM python:3.7


# prepare fs env
RUN mkdir /code
WORKDIR /code

# install dependencies
ADD requirements.txt /code/
RUN pip install -r requirements.txt

#add code
ADD . /code/


EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "bills_service:app", "--log-level=debug"]

