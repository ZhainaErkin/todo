from django.shortcuts import render,HttpResponse,redirect
from .models import ToDo
# Create your views here.


def homeworkk (request):
    return render(request,"index.html")


def test (request):
    todo_list = ToDo.objects.all()

    return render(request,"test.html", {"todo_list": todo_list})

# def homepage(request):
#     return HttpResponse('Добро пожаловать в приложение ToDo - Admin')

 
def check(request):
    return HttpResponse('Проверка')

# def add_todo(request):
#     form = request.POST
#     t = form["todo_text"]
#     todo = ToDo(text=t)
#     todo.save()

#     return redirect(test)   
   
from datetime import datetime

def add_todo(request):
    form = request.POST
    t = form["todo_text"]
    now = datetime.now()
    todo = ToDo(text=t, date=now)
    todo.save()
    return redirect(test)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()  
    return redirect(test)  

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite=True
    todo.save()
    return redirect(test)  

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite=False
    todo.save()
    return redirect(test)    