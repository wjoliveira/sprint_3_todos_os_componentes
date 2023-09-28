FROM python:3.9

WORKDIR /home/python/app

COPY . .

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
