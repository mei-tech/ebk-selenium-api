FROM alpine:3.7

COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN apk --no-cache add  \
        python \
        py-pip \
    && pip install -r requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED 1

CMD ["python", "example.py"]
