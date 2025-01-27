python manage.py migrate
python manage.py collectstatic --noinput
gunicorn django_blog.wsgi:application -c config/gunicorn.conf.py