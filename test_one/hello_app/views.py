from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

def print_hello(request):
    movie_data = {'movie_list' : [
        {
        "movie_name":"movie_one",
        "summary":"sample_name for a movie",
        "year": 2023,
        "success": True
        },
        {
        "movie_name":"movie_two",
        "summary":"",
        "year": 2023,
        "success": True
        },
        {
        "movie_name":"movie_three",
        "summary":"sample_name for a movie",
        "year": 2023,
        "success": True
        },
        {
        "movie_name":"movie_four",
        "summary":"sample_name for a movie",
        "year": 2023,
        "success": True
        },
        {
        "movie_name":"movie_five",
        "summary":"sample_name for a movie",
        "year": 2023,
        "success": True
        },
    ]
}
    return render(request,'sample.html',movie_data)