from django.db import models

class ToDo(models.Model):
  text = models.CharField(max_length=100)
  date=models.DateTimeField(auto_now_add=False)
  is_closed =models.BooleanField(default=False)
  is_favorite=models.BooleanField(default=False)



  

class ToMeet(models.Model):
    person = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    date_of_meeting = models.DateField()
    comment = models.TextField(blank=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

