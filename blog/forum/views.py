from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.


def LikeView(request, pk):
    # which post is being liked
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        # save
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

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

        things = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = things.total_likes()

        liked = False
        if things.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["ops_menu"] = ops_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class PostCreateView(CreateView):
    model = Post
    # designate the form to be used
    form_class = PostForm
    template_name = 'post_add.html'
    # designate fields to show
    # fields = '__all__'


class CommentCreateView(CreateView):
    model = Comment
    # designate the form to be used
    form_class = CommentForm
    template_name = 'add_comment.html'
    # designate fields to show
    # fields = '__all__'
    ordering = ['-date_added']

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})

    # "hi-jack" and replace the post
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


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
