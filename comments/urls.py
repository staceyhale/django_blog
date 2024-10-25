from django.urls import path

from comments.views import delete_comment_view, create_comment_view

app_name = 'comments'

urlpatterns = [
    path('comments/create/', create_comment_view, name='create'),
    path('comments/delete/', delete_comment_view, name='delete'),
]
