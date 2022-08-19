from django.shortcuts import render
from movie.models import Movie
from django.views.generic import ListView, DetailView

class MovieList(ListView):
    model = Movie
    # context_object_name = ''
    # template_name = ''

class MovieDetail(DetailView):
    model = Movie
    # template_name = ''