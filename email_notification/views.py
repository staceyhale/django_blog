from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages


from email_notification.forms import ContactForm, EmailSubscriptionForm
from .services import process_contact_form
from .tasks import send_hello_email


class Contact(View):
    template_name = 'blog/menu/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            process_contact_form(form, request)
            messages.success(self.request, 'Вы успешно отправили письмо')
            form = self.form_class()
        else:
            messages.error(self.request, 'Ошибка отправки письма')
            form = self.form_class()

        return render(request, self.template_name, {'form': form})


class SubscribeEmail(View):
    form_class = EmailSubscriptionForm
    success_url = reverse_lazy('home')

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user_email = form.cleaned_data.get('email')
            send_hello_email.delay(user_email)
            messages.success(self.request, 'Вы подписались на рассылку')
            return redirect(self.success_url)
        messages.error(self.request, 'Ошибка подписки')
        return redirect(self.success_url)
