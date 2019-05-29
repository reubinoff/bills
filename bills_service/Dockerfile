FROM python:3.7


# prepare fs env
RUN mkdir /code
WORKDIR /code

# install dependencies
ADD requirements.txt /code/
RUN pip install -r requirements.txt

#add code
ADD . /code/

CMD ["gunicorn", "-b", "0.0.0.0:${PORT}", "bills_service:app", "--log-level=debug"]

