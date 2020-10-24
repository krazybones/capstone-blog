from django.urls import path
from .views import RegisterView, EditView


urlpatterns = [
    # path('', views.home, name="home"),
    path('register/', RegisterView.as_view(), name='register'),
    path('edit_profile/', EditView.as_view(), name='edit-profile'),
]
