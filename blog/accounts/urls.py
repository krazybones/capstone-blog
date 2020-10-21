from django.urls import path
from .views import RegisterView


urlpatterns = [
    # path('', views.home, name="home"),
    path('register/', RegisterView.as_view(), name='register'),
]
