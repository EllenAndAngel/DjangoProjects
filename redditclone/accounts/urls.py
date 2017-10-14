from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.user_signup, name='signup'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),

]
