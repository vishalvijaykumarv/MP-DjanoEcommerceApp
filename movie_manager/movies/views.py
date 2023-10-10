from django.shortcuts import render
from .  models import MovieInfo
from . form import MovieForm
# Create your views here.

def create(request):
    frm = MovieForm()
    if request.POST:
        # print(request.POST)
        frm = MovieForm(request.POST)
        if frm.is_valid:
            frm.save()
        # title = (request.POST.get('title'))
        # year = (request.POST.get('year'))
        # summary = (request.POST.get('description'))
        # movie_obj=MovieInfo(title=title,year=year,description=summary)
        # movie_obj.save()

    return render(request,'create.html',{'frm':frm})

def list(request):
    movie_data=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_data})

def edit(request):
    return render(request,'edit.html')