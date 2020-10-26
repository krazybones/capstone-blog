from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm, PasswordForm
from forum.models import Profile

# Create your views here.


class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user-profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ProfilePageView, self).get_context_data(
            *args, **kwargs)

        # to grab just the single user view the profile page
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


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
