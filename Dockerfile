From python:3.9

RUN mkdir /VideoSync

WORKDIR /VideoSync

RUN pip install pipenv

copy ./Pipfile.lock /VideoSync/

RUN pipenv install --ignore-pipfile