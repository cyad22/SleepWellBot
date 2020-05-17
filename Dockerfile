FROM python:3
WORKDIR /code
ADD sleepwellbot/main.py .
ADD sleepwellbot/requirements.txt .
RUN pip install --upgrade pip3 && pip3 install -r ./requirements.txt
CMD ["python", "./main.py"]
