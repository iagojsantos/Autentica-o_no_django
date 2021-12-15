from django import urls
from django.urls import path
from django.urls import URLPattern
from core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name= 'index'),
]
