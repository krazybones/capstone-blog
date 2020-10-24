from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import RegisterForm

# Create your views here.


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class EditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
