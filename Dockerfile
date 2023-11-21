FROM python:3.11

# set work directory
WORKDIR /usr/src/cap

# intsall dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/cap
RUN pip install -r requirements.txt

COPY . /usr/src/cap

EXPOSE 8000

CMD ["python", ",manage.py","runserver","0.0.0.0:8000"]

