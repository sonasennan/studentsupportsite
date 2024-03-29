"""
URL configuration for helpmate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from assignment import views
app_name="assignment"

urlpatterns = [
    path('teacher',views.teacher,name="teacher"),
    path('upload/<int:p>',views.upload,name="upload"),
    path('uploadassignment/<p>',views.uploadassignment,name="uploadassignment"),
    path('myassignments',views.myassignments,name="myassignments"),
    path('edit/<int:p>',views.edit,name="edit"),
    path('teachersassignment',views.teachersassignment,name="teachersassignment"),
    path(':deleteassignment/<int:p>',views.deleteassignment,name="deleteassignment"),



]


