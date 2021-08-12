from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Movie

def index(request):
  movies = Movie.objects.all()
  context = {
    "movies": movies
  }
  return render(request, "movies/index.html", context)

def show(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  return render(request, "movies/show.html", { 'movie': movie })

def edit(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  return render(request, "movies/edit.html", { 'movie': movie })

def update(request, movie_id):
  # movie.POST["Title"]
  return HttpResponseRedirect(reverse('movies:show', args=(movie_id,)))