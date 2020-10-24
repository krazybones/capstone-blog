from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm, PasswordForm

# Create your views here.


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordForm
    success_url = reverse_lazy('password_success')


def password_sucess(request):
    return render(request, 'registration/password_sucess.html', {})


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class EditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/profile_edit.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
