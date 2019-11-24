FROM python:3

ADD main.py /
ADD requirements.txt /
CMD ["pip3", "install", "-r", "./requirements.txt"]
CMD ["python", "./main.py"]
