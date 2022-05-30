from django.shortcuts import render
# def index(request):
#     return render(request,'apiTestapp/index.html')
#1===========================Function Base View ==================================

#in api  we don't need "FUNCTION BASE view" To run  html pages 

from rest_framework.decorators import api_view #add decorator apiview: 
from rest_framework.response import Response

                                    # DRF :Django REST Framwork:
    #Browsers capable of executing GET  not POST,but POSTMAN help us Execute them as POST,GET and etc!
        # Postman (a software from google for testing api ) can help you Test instead of  URL

            # If we would like to execute api using 'Function Base' we should add  decorator : @api_view
    # @api_view(['GET','POST']) #Indicates types of ( GET , POST ):our methods work base on the methods said:
                # style of  transfer and recieve the datas ! Post, get,delete, put methos!
#Example 1:
# @api_view(['GET']) #we used Funcation Based for api 
# def api_index(request): 
#     context={
#         'name':'Max Jokar'
        
#     }
#     return Response(context)
#127.0.0.1.8000/api/index/  Runs the above Code:

#2==============================CLASS BASE VIEW=====================================
# THE BELOW METHOD IS BETTER THAN ABOVE

    #APIView class:whenever you want to define a "ClassBase" it should be child of  "APIView":
                    # from rest_framework.views import APIView
                # from rest_framework.response import Response
                        #needs to inherit from the APIView 
#Example2:                       
# class IndexApi(APIView):   #Method "GET" :if we want to define a Class Base , it should be child of APIView!It has many methods like def get,post etc.
#     def get(self,request):         #the name of funcation determines its procedure = GET or POST :
#         context={
#             'name':'Max Jokar',
#             'family':'jokar'
        
#     }
#         return Response(context)

# Call by Parameters:api  can send "GET" or post data to this api
#like:name , age , family 


#Example 3: make a api with Paramter in its URL :(Call by  Parameters)
# from rest_framework.views import APIView
# from rest_framework.response import Response
# class IndexApi2(APIView): 
#     def get(self,request,name,family,age): #URL should have Parameter too(api with Parameters)
#         context={
#             'name':name, 
#             'family':family,
#             'age':age
        
#         }
#         return Response(context)
#http://Name of your  site  .com/api/indexapi/John/Kambel/28

#Example 4 .use Request :data sent by "query string" :our request be possible to opened============================

# from rest_framework.views import APIView
# from rest_framework.response import Response

# class IndexApi3(APIView): 
#     # def get(self,request):#receive from the body of the  Transfer
#     def post(self,request):#This method is also possible but we better use Postman
#         name=request.query_params.get('name')
#         # name=request.query_params.get['name']
#         # name=request.GET['name'] #get data from query string of  Address
#         family=request.GET.get('family') 
#         age=request.GET.get('age') 

       
#         context={
#             'name':name, 
#             'family':family,
#             'age':age
        
#         }
#         return Response(context)

#api/IndexApi3==>?name=Max&family=Jokar&age=42 :check in Postman 
#in Postman we fill keys:name,family ,age with Parameters.
 

#5 Serialize :objects(Models:Packed datas as a Model) & should be ready to transmit means Serialized

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .Serializers import PersonSerializers,ProductSerializers
from rest_framework import status
 
class PersonList(APIView):
    def get(self,request):
        people=Person.objects.all() #***From here we should  Serialize because Person is already an Object or Model,
        # means that object datas should be transfered  to  with  Datas  as file stream templates which capable to transmit 
        #Hence,we make a module named:Serializers.py :Serializers.py  Method 1st
        # we import PersonSerializers
        
        #ser_data is the people which is serialized to ser...
        ser_data=PersonSerializers(instance=people,many=True) #for several fields we need many=True 
       #instance is my object:People (name,family, age,...)
        return Response(data=ser_data.data) #only give the data from ser_data .data
        
         #api/people :datas from our database goes to Brower/Postman
    #************************************************************************************************************************    
                                #Exercise to serarch in Database:
#6 Search a Person from Our list by recieving  on ID :http://127.0.0.1:8000/api/people/2/     
class SearchPersonById(APIView): #Class Base which is child of  APIView is a very good Method 
    def get(self,request,code):#To get Id  The user sends  ID .1
        try:
            person=Person.objects.get(id=code) #2
            #ser_data is the people which is serialized to ser...
            ser_data=PersonSerializers(instance=person) #My object which I want to give it to serilizer=Serialize
            return Response(data=ser_data.data)   #You give Answer to User (contains Information)
        except:    
            return Response("Not Found ")
        
#api/people/2/  we can see the  person with the id :2     

   
#To delete, Create , Update with POST=============!Post:Deserialize=================                                           
                # ExerciseADD :we want to register inside the Person :
   
class PersonAdd(APIView):# we will use Postman , fill in fields in Body ,form-data:
    def post(self,request): #request is data sent from User:
        #Deserilize:Data recieved  from User & give to Serializer 
        ser_data=PersonSerializers(data=request.POST) # (Deserialize)from the User api comes:data=Those Jason data from User applicant for api sent to us 
        #request.POST :takes text or words data
        if ser_data.is_valid():
            #To get datas we use create:
            Person.objects.create(
                name=ser_data.validated_data['name'],
                family=ser_data.validated_data['family'],
                email=ser_data.validated_data['email'],
                age=ser_data.validated_data['age'],
                username=ser_data.validated_data['username'],
                password=ser_data.validated_data['password'],
                
            ) #if Ok return  status 201
            #import status
            return Response(data=ser_data.data,status=status.HTTP_201_CREATED) #statur:codes are  related to http 
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
#in Postman we make fields, KEY  fill in them then check with our website:  
    
#5.6====================================================================================
#import ProductSerializers
class ProductAdd(APIView):
    def post(self,request):
        ser_data=ProductSerializers(data=request.data)#gets data from type of  text or data file 
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data,status=status.HTTP_201_CREATED) #statur:codes are  related to http 
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
   
    
    
    
    
     
    
    
    

        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
       