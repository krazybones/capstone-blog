from django.urls import path
# from . import views
from .views import HomeView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CategoryCreateView, CategoryView, CategoryListView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', PostCreateView.as_view(), name='post-add'),
    path('add_category/', CategoryCreateView.as_view(), name='category-add'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('category/<str:ops>/', CategoryView, name="category-view"),
    path('category-list/', CategoryListView, name="category-list"),
]
