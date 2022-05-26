from django.contrib import admin
from django.urls import path,include
from django.conf import settings #to use  setting in +static we should add this part
from django.conf.urls.static import static #aslo required after +setting To be recognized  


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('apps.mainapp.urls')),
    # path('blog/',include('apps.blog.urls')),
    # path('formtest/',include('apps.formtest.urls')),
    # path('post/',include('apps.viewtest.urls'),name='post'),
    path('api/',include('apps.apiTestApp.urls'),name='apiTest'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#this static added after  media_url in step10 is used in  