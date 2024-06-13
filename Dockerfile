FROM python:3.10

RUN useradd -m -u 1000 user

COPY --chown=user . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD gunicorn -b 0.0.0.0:8000 web:app & python main.py