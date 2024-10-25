import logging

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView

from user.forms import RegisterForm, LoginForm, UserProfileForm
from user.models import CustomUser
from user.services import register_user, login_user, get_user_profile_by_username

logger = logging.getLogger(__name__)


class RegisterView(View):
    template_name = 'user/forms/register.html'
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if register_user(form, request):
            return redirect('user:login')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'user/forms/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if login_user(form, request):
            return redirect('home')

        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user:login')


class ProfileView(DetailView):
    model = CustomUser
    context_object_name = 'profile'
    template_name = 'user/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Страница пользователя: {self.object.user.username}'
        return context

    def get_object(self, queryset=None):
        username = self.kwargs.get('user')
        return get_user_profile_by_username(username)


@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    template_name = 'user/user_profile_edit.html'

    def get(self, request, user):
        user_profile = get_user_profile_by_username(user)
        form = UserProfileForm(instance=user_profile)

        context = {
            'form': form,
            'title': f'Редактировать профиль: {user_profile.user.username}',
        }
        return render(request, self.template_name, context)

    def post(self, request, user):
        user_profile = get_user_profile_by_username(user)
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user_profile)

        # if update_profile:
        if form.is_valid():
            form.save()
            return redirect('user:profile', user=user_profile.user.username)

        context = {
            'form': form,
            'title': f'Редактировать профиль: {user_profile.user.username}',
        }
        return render(request, self.template_name, context)

