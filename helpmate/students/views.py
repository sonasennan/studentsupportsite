from django.shortcuts import render,redirect
from students.models import Notes
from students.models import Questionpapers,CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'home.html')

def firstyear(request):
    return render(request,'firstyear.html')

def secondyear(request):
    return render(request,'secondyear.html')

def thirdyear(request):
    return render(request,'thirdyear.html')

@login_required
def getnotes(request,p):
    notes=Notes.objects.filter(year=p)
    return render(request,'getnotes.html',{'notes':notes})

@login_required
def getquestionpapers(request,p):
    questions=Questionpapers.objects.filter(year=p)
    return render(request,'getquestionpapers.html',{'questions':questions})

@login_required
def student_register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p1=request.POST['p1']
        p2=request.POST['p2']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']
        m=request.POST['m']
        if(p1==p2):
            u=CustomUser.objects.create_user(username=u,password=p1,email=e,first_name=f,last_name=l,phone=m)
            u.is_student=True
            u.save()
            return log(request)
    return render(request,'student_register.html')


@login_required
def teacher_register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p1=request.POST['p1']
        p2=request.POST['p2']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']
        m=request.POST['m']
        if(p1==p2):
            u=CustomUser.objects.create_user(username=u,password=p1,email=e,first_name=f,last_name=l,phone=m)
            u.is_teacher=True
            u.save()
            return log(request)
    return render(request,'teacher_register.html')

def log(request):
    return render(request,"log.html")


def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p1=request.POST['p1']
        user=authenticate(username=u,password=p1)
        if user and user.is_student==True:
            login(request,user)
            return render(request,'home.html')
        elif user and user.is_teacher==True:
            login(request,user)
            return render(request,'home.html')
        else:
            messages.error(request,"Invalid Credentials")

    return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return user_login(request)


@login_required
def addnotes(request):
    if(request.method=="POST"):
        s=request.POST['s']
        f=request.FILES['f']
        y=request.POST['y']
        t=request.POST['t']
        n=Notes.objects.create(subject=s,pdf=f,year=y,type=t)
        n.save()
        return action(request)

    return render(request,"addnotes.html")

def action(request):
    return render(request,"action.html")

