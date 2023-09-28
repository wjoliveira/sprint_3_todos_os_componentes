FROM python:3.9

WORKDIR /home/python/app

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

#CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

RUN flask run --host 0.0.0.0 --port 5000