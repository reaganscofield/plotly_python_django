from django.conf.urls import url
from django.urls import  include, path
from django.contrib import admin

urlpatterns = [
    # include app url patterns from app directory
    path('', include('app.urls')),  
]
