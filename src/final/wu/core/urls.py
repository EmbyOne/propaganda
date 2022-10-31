from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    #path('juhiload/', views.license),
    #re_path(r'^storage/(?P<filename>license\d+\.png)/$', views.storage),
]