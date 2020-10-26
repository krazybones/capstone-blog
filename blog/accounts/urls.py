from django.urls import path
from .views import RegisterView, EditView, PasswordsChangeView, ProfilePageView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path('', views.home, name="home"),
    path('register/', RegisterView.as_view(), name='register'),
    path('edit_profile/', EditView.as_view(), name='edit-profile'),
    path('password/', auth_views.PasswordChangeView.as_view(
        template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(
        template_name='registration/change-password.html')),
    path('password_success', views.password_sucess, name='password-success'),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile-page'),
]
