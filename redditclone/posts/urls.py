from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^addpost/', views.add, name='addpost'),
    url(r'(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    url(r'(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),

]
