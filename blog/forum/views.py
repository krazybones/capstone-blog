from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.


# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    # first define which model to use
    model = Post
    # which file to use
    template_name = 'home.html'


class PostDetailView(DetailView):
    # same setup as HomeView
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_add.html'
    # designate fields to show
    fields = '__all__'
