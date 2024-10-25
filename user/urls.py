from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileView, EditProfileView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<str:user>/', ProfileView.as_view(), name='profile'),
    path('profile/<str:user>/edit/', EditProfileView.as_view(), name='profile_edit'),

]


