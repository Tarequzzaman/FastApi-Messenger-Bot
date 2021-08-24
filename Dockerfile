FROM python:3.7

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8001

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]