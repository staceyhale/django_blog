from django.urls import path

from .views import Contact, SubscribeEmail

app_name = 'email'

urlpatterns = [
    path('post_subscribe/', SubscribeEmail.as_view(), name='post_subscribe'),
    path('contact/', Contact.as_view(), name='contact'),
]
