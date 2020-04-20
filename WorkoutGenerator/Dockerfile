From ubuntu:latest

Maintainer Brendan Griffin "brendankgriffin@hotmail.com"

Run apt-get update -y && \
    apt-get install -y python-pip python-dev

Copy ./requirements.txt /app/requirements.txt

Workdir /app

Run pip install -r requirements.txt

Copy . /app

ENTRYPOINT ["python"]
CMD ["WorkoutGenerator.py"]