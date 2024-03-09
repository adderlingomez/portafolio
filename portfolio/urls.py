from django.contrib import admin
from django.conf.urls import include, urls
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',      admin.site.urls),
    path('',            views.inicio, name='inicio' ),
    path('portafolio/', views.portafolio, name='portafolio' ),
    path('contacto/',   views.contacto, name='contacto' ),
    url()
]
