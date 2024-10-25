from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from comments.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ('content', 'captcha')
        widgets = {"content": forms.Textarea(attrs={"class": ""})}

