from cProfile import label
from django.db import models
from django.utils import timezone


# class Post(models.Model):
#     title=models.CharField(max_length=50,verbose_name="Title of Post")
#     description=models.TextField(max_length=300,verbose_name="Description")
#     is_active=models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.title +" "+self.description +" "+str(self.is_active)

class Person(models.Model):
    name=models.CharField(max_length=20)
    family=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    age=models.PositiveIntegerField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=60)


def __str__(self):
    return f"{self.name}:{self.family} {self.email} {self.username}"


















