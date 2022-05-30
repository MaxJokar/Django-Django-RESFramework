from rest_framework import serializers


# Method 1:From Model Make the same field for  OUr  Serializer Below:PersonSerializers
    #Fields from our Model are Copied the same for serializers:serializers.Serializer
    #Our Model:class Person(models.Model):
    # name=models.CharField(max_length=20)
    # family=models.CharField(max_length=30)
    # email=models.EmailField(max_length=30)
    # age=models.PositiveIntegerField()
    # username=models.CharField(max_length=30)
    # password=models.CharField(max_length=60)

# class PersonSerializers(serializers.Serializer):
#     name=serializers.CharField(max_length=20)
#     family=serializers.CharField(max_length=30)
#     email=serializers.EmailField(max_length=30)
#     age=serializers.IntegerField()
#     username=serializers.CharField(max_length=30)
#     password=serializers.CharField(max_length=60)



#Method 2nd :Model Serializer ================META class=============serializers.ModelSerializer
 
#The previous Method was not so  Professional , but Belowe we would like to introduce you a 
#Model Serialzer  which is more professional :Model, Serialzier !
#Model Serializer:instead to defining feilds we define a META Class 
#in Meta class  ,weindicate   What is suppose to Convert by our Class PersonSerialiser  
#import Person
from .models import Person
class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model=Person #This definition is equal all fields we describe above(nam,family, email,...)
        # fields="__all__" #support all our fields (name, family , etc,...)
        # fields=["name","family","age","email"]     #we have just these fields
        
        exclude=["password"] # deny to show password , Above must be off:http://127.0.0.1:8000/api/people/
#with above syntax we can control access to the fields!

#===========================================================================================

# For  validator or Upload  5.2 first Make models
#The below class can both serialize and Deserialize :
from .models import Product
class ProductSerializers(serializers.ModelSerializer): 
    class Meta:
        model=Product      
        fields="__all__"
        
        #api/people/    3.../
        
        


