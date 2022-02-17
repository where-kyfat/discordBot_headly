FROM python:3.9
WORKDIR /bot/
COPY config.py /bot/
COPY main.py /bot/
COPY requirements.txt /bot/
RUN pip install -r requirements.txt