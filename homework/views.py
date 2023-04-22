from django.shortcuts import render,HttpResponse
from .models import ToDo
# Create your views here.


def homeworkk (request):
    return render(request,"index.html")


def test (request):
    todo_list = ToDo.objects.all()

    return render(request,"test.html", {"todo_list": todo_list})

def homepage(request):
    return HttpResponse('Добро пожаловать в приложение ToDo - Admin')

 
def check(request):
    return HttpResponse('Проверка')
   
