from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Movie
from .forms import MovieForm

def index(request):
  movies = Movie.objects.all()
  context = {
    "movies": movies
  }
  return render(request, "movies/index.html", context)

def show(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  return render(request, "movies/show.html", { 'movie': movie })

def create(request):
  form = MovieForm(request.POST or None)
  if form.is_valid():
    movie = form.save()
    return HttpResponseRedirect(reverse('movies:show', args=(movie.id,)))
  return render(request, "movies/create.html", { 'form': form })

def edit(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  form = MovieForm(request.POST or None, instance=movie)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('movies:show', args=(movie_id,)))
  return render(request, "movies/edit.html", { 'movie': movie, 'form': form })

def update(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  form = MovieForm(request.POST or None, instance=movie)
  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('movies:show', args=(movie_id,)))
  movie = Movie.objects.get(pk=movie_id)
  movie.title = request.POST['title']
  movie.save()

def delete(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  movie.delete()
  return HttpResponseRedirect(reverse('movies:index'))

