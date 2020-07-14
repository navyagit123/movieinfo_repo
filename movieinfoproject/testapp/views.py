from django.shortcuts import render
from testapp.forms import movieform
from testapp.models import movie

# Create your views here.
def homeview(request):
    return render(request,'testapp/home.html')

def addmovie(request):
    form=movieform()
    if request.method=='POST':
        form=movieform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return homeview(request)
    return render(request,'testapp/addmv.html',{'form':form})

def updatemovie(request):
    movie_list=movie.objects.all()
    return render(request,'testapp/updatemv.html',{'movie_list':movie_list})
