from cProfile import label
from django.db import models
from django.utils import timezone


# class Post(models.Model):
#     title=models.CharField(max_length=50,verbose_name="Title of Post")
#     description=models.TextField(max_length=300,verbose_name="Description")
#     is_active=models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.title +" "+self.description +" "+str(self.is_active)
#=============================================For Serialize 1. then  make Serializers.py 2.=========================
class Person(models.Model):
    name=models.CharField(max_length=20)
    family=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    age=models.PositiveIntegerField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=60,null=True,blank=True) #for password database needs something to populate exisiting rows(null and blan need)

def __str__(self):
    return f"{self.name}:{self.family} {self.email} {self.username}"
#=py manage.py makemigrations ,   migrate  =====check database

#==============================Upload files in our  DataBase:====================
#To ImageField(upload_to):get its Address & its name  from one Function=

import datetime 
#5.1.5use validator or Upload  ++++++++++++++++++++++++++++5
#we want our upload_to gets its address from a method :upload to can be a invite a definition (a.jpg)
def image_path(instance,filename):#instance,is a photo ,filename is a name for  file  :
    ext=filename.split('.')[-1]#for format                                   jpg
    name=filename.split('.')[0]#name of file is splitted from its pasvand     a
    current_date=datetime.datetime.utc.now().strftime("%Y%m%D%H%M%S")
    return f"images/products/{name}_{current_data}.{ext}" #5.4
 # result:  images/products/a_20220615.jpg



class Product(models.Model):
    name=models.CharField(max_length=200,)#gets from User
    price=models.IntegerField()#gets from User
    register_date=models.DateField(auto_now_add=True,)#automatically fills during adding
    #5.5 image=models.ImageField(upload_to="")#we should give specific address for upload 
    image=models.ImageField(upload_to="image_path",default="images/products/nophoto.svg")#saves here:images/products...add()
    
    def __str__(self):
        return f"{self.name } {self.price}"
    
    
#5.2 we will write its serializer then :we go to serializer.py 
#we want our upload_to gets its address from a method :upload to can be a invite a definition 
#5.3 make a Folder in media  Products 
















    
    
    
    
    
    
    













