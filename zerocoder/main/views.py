from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

# def data(request):
#     return HttpResponse("<h1>Это третья страница моего проекта на Django, которая называется data.</h1>")
#
# def test(request):
#     return HttpResponse("<h1>Это четвертая страница моего проекта на Django, которая называется test.</h1>")
