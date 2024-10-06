from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Это мой второй проект на Django!</h1>')

def about(request):
    return HttpResponse('<h1>Это вторая страница моего второго проекта на Django!</h1>')