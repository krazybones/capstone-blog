from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.


# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    # first define which model to use
    model = Post
    # which file to use
    template_name = 'home.html'
    ordering = ['-post_date']
    # new ordering won't take affect till after Blog 6

    # passing the Category menu to the navbar
    def get_context_data(self, *args, **kwargs):
        # Category model only has 1 parameter hence no need to filter below:
        ops_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["ops_menu"] = ops_menu
        return context


def CategoryListView(request):
    # querying the database for all Categories and assigning them a variable name
    ops_menu_list = Category.objects.all()
    # passing the variable to the page via variable
    return render(request, 'category_list.html', {'ops_menu_list': ops_menu_list})


def CategoryView(request, ops):
    category_posts = Post.objects.filter(category=ops)
    return render(request, 'categories.html', {'ops': ops.title(), 'category_posts': category_posts})


class PostDetailView(DetailView):
    # same setup as HomeView
    model = Post
    template_name = 'post_detail.html'

    # must pass below function in every view desired
    def get_context_data(self, *args, **kwargs):
        # Category model only has 1 parameter hence no need to filter below:
        ops_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context["ops_menu"] = ops_menu
        return context


class PostCreateView(CreateView):
    model = Post
    # designate the form to be used
    form_class = PostForm
    template_name = 'post_add.html'
    # designate fields to show
    # fields = '__all__'


class CategoryCreateView(CreateView):
    model = Category
    # designate the form to be used
    template_name = 'category_add.html'
    # designate fields to show
    fields = '__all__'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'title_tag', 'body']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
