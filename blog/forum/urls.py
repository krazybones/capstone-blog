from django.urls import path
# from . import views
from .views import HomeView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', PostCreateView.as_view(), name='post-add'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='post-edit'),
]
