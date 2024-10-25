from django.core.mail import send_mail
# from .tasks import send_hello_email


def process_contact_form(form, request):
    contact = form.save(commit=False)
    contact.profile = request.user.userprofile
    form.save()


def send_email(user_email):
    send_mail(
        'Вы подписались на рассылку моего сайтика!',
        'Проверка отправки с сайтика через форму рассылки c помощью celery. :3',
        'djangotestprojectnews@gmail.com',
        [user_email],
        fail_silently=False
    )
