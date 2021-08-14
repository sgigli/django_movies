from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'registration/signup.html'





# from django.urls import reverse_lazy
# from .forms import UserRegisterForm
# from django.contrib.messages.views import SuccessMessageMixin
# from django.views.generic.edit import CreateView

# class SignUpView(SuccessMessageMixin, CreateView):
#   template_name = 'users/register.html'
#   success_url = reverse_lazy('login')
#   form_class = UserRegisterForm
#   success_message = "Your profile was created successfully"

