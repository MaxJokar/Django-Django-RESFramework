from django.shortcuts import render
# def index(request):
#     return render(request,'apiTestapp/index.html')
#============================================================================

#FUNCTION BASE VIEW:
#DRF :Django REST Framwork:
# from rest_framework.decorators import api_view #add decorator apiview: 
# from rest_framework.response import Response

#Postman can help you Test instead of  URL 
#indicates style of  transfer and recieve the datas ! Post, get,delete, put methos!
# @api_view(['GET','POST']) #the methods are GET , POST :our methods works base on the methods said:
# @api_view(['GET'])
# def api_index(request): 
#     context={
#         'name':'Max Jokar'
        
#     }
#     return Response(context)

#==2====THE BELOW METHOD IS BETTER THAN ABOVE ==============================
#CLASS BASED VIEW

#APIView class:whenever you want to define a ClassBase it should be child of  APIView:
# from rest_framework.views import APIView
# from rest_framework.response import Response
#needs to inherit from the apiview 
# class IndexApi(APIView): 
    # def get(self,request):#the name of funcation determines its procedure = GET or POST :
    #     context={
    #         'name':'Max Jokar',
    #         'family':'jokar'
        
    # }
    #     return Response(context)

#3 Call by Parameters:we wnat to make api which the user can send or post data to this api
#like:name , age , family 


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


#4===use Request :data sent by "query string" :our request be possible to opened

# from rest_framework.views import APIView
# from rest_framework.response import Response

# class IndexApi3(APIView): 
#     # def get(self,request):#receive from the body of the  Transfer
#     def post(self,request):
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




#5 Seriazie ==================Serializer :objects  =we will write and api which gives List of person list inside of our database:

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .Serializers import PersonSerializers

class PersonList(APIView):
    def get(self,request):
        people=Person.objects.all()
        #ser_data is the people which is serialized to ser...
        ser_data=PersonSerializers(instance=people,many=True) #for several we need many=True 
        return Response(data=ser_data.data)
        
        
        
  #6 Search a Person from Our list by recieving  on ID :http://127.0.0.1:8000/api/people/2/     
class SearchPersonById(APIView):
    def get(self,request,code):#The user sends  ID .1
        try:
            person=Person.objects.get(id=code) #2
            #ser_data is the people which is serialized to ser...
            ser_data=PersonSerializers(instance=person)
            return Response(data=ser_data.data)   
            
            
        except:    
            return Response("Not Found ")
        
        
        #Exercise!Post
# ADD :Enrolment class  :we want to register inside the Person :
#7 For Create, Update , Delete  use  POST  method :
    
class PersonAdd(APIView):
    def post(self,request):
        ser_data=PersonSerializer(data=request.POST)
        if ser_data.is_valid():
            Person.objects.create(
                name=ser_data.validated_data['name'],
                family=ser_data.validated_data['family'],
                email=ser_data.validated_data['email'],
                age=ser_data.validated_data['age'],
                username=ser_data.validated_data['username'],
                passsword=ser_data.validated_data['passsword'],
                
            )
            return Response(data=ser_data.data)
        return Response(ser_data.errors)
        
    
    
    
    
    
    
    
    
        
        
       