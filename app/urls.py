from django.conf.urls import url
from . import views
from django.urls import path

# register urls 
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name="register"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard2', views.dashboard, name='dashboard'),
    path('read', views.read, name='read'),
    path('carousel', views.carousel, name='carousel'),
    path('plotlygraph', views.plotlygraph, name='plotlygraph'),
]
 