
from django.urls import path 
import apps.mainapp.views as views



urlpatterns = [
    path('',views.index,name='index'),
    
]
