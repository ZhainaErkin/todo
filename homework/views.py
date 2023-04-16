from django.shortcuts import render,HttpResponse

# Create your views here.


def homeworkk (request):
    return render(request,"index.html")

def homepage(request):
    return HttpResponse('Добро пожаловать в приложение ToDo - Admin')

 
def check(request):
    return HttpResponse('Проверка')
   
