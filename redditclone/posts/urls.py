from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^addpost/', views.add, name='addpost'),


]