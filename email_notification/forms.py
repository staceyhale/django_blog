from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from email_notification.models import Contact, EmailSubscription


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    subject = forms.CharField(label='Тема',
                              widget=forms.TextInput(attrs={"class": "form-control"}),
                              )
    email = forms.EmailField(label='Электронная почта',
                             widget=forms.TextInput(attrs={"class": "form-control"})
                             )
    content = forms.CharField(label='Текст',
                              widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}),
                              )

    class Meta:
        model = Contact
        fields = ('subject', 'email', 'content', 'captcha')


class EmailSubscriptionForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = EmailSubscription
        fields = ('email', 'captcha')
        widgets = {"email": forms.TextInput(attrs={"class": "form-control"})}

