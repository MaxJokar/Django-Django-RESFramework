from django.urls import path 
import apps.apiTestApp.views as views



urlpatterns = [
    # path('',views.index,name='index'),
    # path('index/',views.api_index,name='api_index'),
    # path('indexapi/',views.IndexApi.as_view()),     #as_view :because IndexApi is  Class & inside view IndexApi we should mentioin this way :
    # path('indexapi/<str:name>/<str:family>/<int:age>',views.IndexApi2.as_view()),
    # path('indexapi/',views.IndexApi3.as_view()),
    # path('people/',views.PersonList.as_view()),
    # path('people/<int:code>/',views.SearchPersonById.as_view()),
    # path('people/add/',views.PersonAdd.as_view()),
    path('product/add/',views.ProductAdd.as_view()), #api/product/add
    
    
]
