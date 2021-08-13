from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Movie
from .forms import MovieForm

class IndexView(generic.ListView):
  model = Movie
  template_name = "movies/index.html"

class DetailView(generic.DetailView):
  model = Movie
  template_name = "movies/detail.html"

class CreateView(CreateView):
  model = Movie
  fields = ["title"]
  template_name = "movies/create.html"
  
  def get_success_url(self):
    return reverse('movies:detail', kwargs={'pk': self.object.pk})

class UpdateView(UpdateView):
  model = Movie
  fields = ["title"]
  template_name = "movies/edit.html"

  def get_success_url(self):
    return reverse('movies:detail', kwargs={'pk': self.object.pk})

class DeleteView(DeleteView):
  model = Movie
  success_url = reverse_lazy("movies:index")

