
from django.contrib import admin
from django.urls import path, include
from enviarApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createpost', views.createpost),
    path('createanpost', views.createanpost),
    path('createpostCheckB', views.createpostCheckB),
    path('deletepostCheckB', views.deletepostCheckB),
    path('Papeleria/', views.Papeleria, name='Papeleria'),
    path('createpostButton', views.createpostButton),
    path('deletepostButton', views.deletepostButton),
    path('createCatalogo', views.createCatalogo, name='createCatalogo'),
    path('carritoCompra', views.carritoCompra),
    path('borrarCompra', views.borrarCompra),
    path('agregarCompra', views.agregarCompra),
    path('send_dictionary', views.send_dictionary),
    path('opposites', views.opposites),
    path('headerTemplate', views.headerTemplate),
    path('notPosting', views.notPosting),
    path('sendjson/', views.send_json, name='send_json'),
    path('', views.home, name='home'),
    path('setc', views.setting_cookie, name='setc'),
    path('getc', views.getting_cookie, name='getc'),
     path('slider', views.slider, name='slider')

]
