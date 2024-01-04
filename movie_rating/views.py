from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

def index(request):
    data = {
       "message":"World"
    }
    return render(request, 'index.html', data)

@api_view(['GET'])
def getAllMovies(request):
    movies = Movie.objects.all()
    serialized_movies = MovieSerializer(movies, many=True)
    return Response(serialized_movies.data)
