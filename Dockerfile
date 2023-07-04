FROM python:3.10-slim-bullseye

WORKDIR /middleware-facade

EXPOSE 8000

COPY . .

RUN pip install --no-cache-dir --upgrade pipenv==2022.12.19

RUN pipenv install --deploy

CMD ["pipenv", "run", "gunicorn", "application.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]