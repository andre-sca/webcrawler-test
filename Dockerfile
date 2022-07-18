FROM python:3.9-alpine
RUN apk add gcc g++ make libffi-dev openssl-dev
COPY . /app
WORKDIR /app
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
ENV PYTHONPATH "${PYTHONPATH}:/app/app"
CMD ["-m", "app.__init__"]