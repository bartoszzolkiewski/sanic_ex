FROM python:3.7

LABEL Name=sanic_ex Version=0.0.1
EXPOSE 5000

WORKDIR /app
ADD . /app

# Using pip:
RUN python3 -m pip install -r requirements.txt
CMD ["python3", "./run.py"]

