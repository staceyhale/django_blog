from django_blog.celery import app

from .services import send_email


@app.task()
def send_hello_email(user_email):
    send_email(user_email)

