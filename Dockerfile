FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DOCKER_ENV=1

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY verification_sms /app
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=verification_sms.settings
WORKDIR /app/verification_sms

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
