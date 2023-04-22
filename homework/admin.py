from django.contrib import admin
from .models import ToDo

admin.site.register(ToDo)




# from .models import ToMeet

# class ToMeetAdmin(admin.ModelAdmin):
#     list_display = ('person', 'phone_number', 'date_of_meeting', 'is_closed', 'is_favorite')
#     list_filter = ('is_closed', 'is_favorite')
#     search_fields = ('person', 'phone_number')

# admin.site.register(ToMeet, ToMeetAdmin)








# from django import models

# class Person(models,):
#     name=models.CharField(max_length=20)
#     age=models.IntegerField()
    

# admin.site.register( Person,
# from django import models

# class Person(models,):
#     name=models.CharField(max_length=20)
#     age=models.IntegerField()
    

# admin.site.register( Person,)



# Задание № 3

# Напишите тип данных каждого из перечисленных типов моделей django.

# models.BooleanField()
# models.DateTimeField()
# models.FloatField()
# models.CharField()
# models.EmailField()
# models.TextField()


# Каждый из перечисленных типов полей в Django соответствует 
# определенному типу данных в базе данных:

# models.BooleanField() соответствует типу данных BOOLEAN в базе данных.
# models.DateTimeField() соответствует типу данных DATETIME в базе данных.
# models.FloatField() соответствует типу данных FLOAT в базе данных.
# models.CharField() соответствует типу данных VARCHAR в базе данных. 
# Этот тип поля позволяет хранить строковые данные переменной длины.
# models.EmailField() также соответствует типу данных VARCHAR в базе данных.
#  Он используется для хранения email-адресов и включает проверку на соответствие формату email-адреса.
# models.TextField() также соответствует типу данных TEXT в базе данных.
# Он используется для хранения больших объемов текстовых данных.




