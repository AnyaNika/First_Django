from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")

def data(request):
    return HttpResponse("<h1>Это третья страница моего проекта на Django, которая называется data.</h1>")

def test(request):
    return HttpResponse("<h1>Это четвертая страница моего проекта на Django, которая называется test.</h1>")
