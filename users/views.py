from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.models import User
from .models import Profile

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'registration/signup.html'

class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = Profile
    fields = ["hometown"]
    template_name = 'profile/detail.html'
    success_message = "Profile successfully updated!"

    def get_success_url(self):
        return reverse('users:profile', kwargs={'pk': self.object.pk})

def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'profile/detail.html', { 'user': user })
