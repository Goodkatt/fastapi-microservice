FROM python:3.9

RUN apt update

RUN apt install -y procps \
    curl \
    net-tools \
    wget \
    nginx \
    vim

COPY requirements.txt /var

WORKDIR /var

RUN pip install -r requirements.txt

COPY main.py /code/app/main.py

COPY nginx.conf /etc/nginx/conf.d/nginx.conf

COPY index.html /usr/share/nginx/html/index.html

WORKDIR /code

CMD service nginx start && uvicorn app.main:app --host 0.0.0.0 --port 8000

#ENTRYPOINT [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]

EXPOSE 8080