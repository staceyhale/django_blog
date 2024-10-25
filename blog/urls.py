from django.urls import path

from .views import Home, GetByCategory, GetByTag, GetPost, CategoryMenu, TagsMenu, SocialNetwork, Search

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>', GetByCategory.as_view(), name='category'),
    path('tag/<str:slug>', GetByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    # path('post/<int:post_id>/', GetPost.as_view(), name='post'),
    path('categories/', CategoryMenu.as_view(), name='categories'),
    path('tags/', TagsMenu.as_view(), name='tags'),
    path('networks/', SocialNetwork.as_view(), name='networks'),
    path('search/', Search.as_view(), name='search'),
]

