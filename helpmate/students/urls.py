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
from students import views
app_name="students"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('firstyear',views.firstyear,name="firstyear"),
    path('secondyear', views.secondyear, name="secondyear"),
    path('thirdyear', views.thirdyear, name="thirdyear"),
    path('getnotes/<int:p>',views.getnotes,name="getnotes"),
    path('getquestionpapers/<int:p>',views.getquestionpapers,name="getquestionpapers"),
    path('student_register',views.student_register,name="student_register"),
    path('teacher_register',views.teacher_register,name="teacher_register"),
    path('user_login',views.user_login,name="user_login"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('addnotes',views.addnotes,name="addnotes"),
    path('action',views.action,name="action"),
    path('log',views.log,name="log"),



]
