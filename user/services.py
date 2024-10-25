from django.contrib import messages
from django.contrib.auth import login
from user.models import UserProfile


def register_user(form, request):
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        login(request, user)
        messages.success(request, 'Вы успешно зарегистрировались')
        return True
    else:
        messages.error(request, 'Ошибка регистрации')
        return False


def login_user(form, request):
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return True
    return False


def get_user_profile_by_username(user):
    return UserProfile.objects.get(user__username=user)



