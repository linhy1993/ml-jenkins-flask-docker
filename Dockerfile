# train and run the model with RESTful api
FROM python:3.7.1

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD python /app/train_model.py && python /app/server.py
