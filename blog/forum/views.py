from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    # first define which model to use
    model = Post
    # which file to use
    template_name = 'home.html'
