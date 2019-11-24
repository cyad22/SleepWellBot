FROM python:3
WORKDIR /code
ADD sleepwellbot/main.py /code
ADD sleepwellbot/requirements.txt /code
RUN pip3 install -r ./requirements.txt
CMD ["python", "./main.py"]
