from django.shortcuts import render,redirect
from assignment.models import Teacher,Assignment
from assignment.forms import AssignmentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def teacher(request):
    user=request.user
    if(request.method=="POST"):
        s=request.POST['s']
        y=request.POST['y']
        t=Teacher.objects.create(subject=s,year=y,user=user)
        t.save()
        return redirect('students:home')
    return render(request,"teacher.html")

@login_required
def upload(request,p):
    t=Teacher.objects.filter(year=p)
    return render(request,"upload.html",{'t':t})

@login_required
def uploadassignment(request,p):
    user=request.user
    if(request.method=="POST"):
        n=request.POST['n']
        f=request.POST['f']
        a=Assignment.objects.create(studentname=n,pdf=f,subject=p,user=user)
        a.save()
    return render(request,"uploadassignment.html")


@login_required
def myassignments(request):
    user=request.user
    a=Assignment.objects.filter(user=user)
    return render(request,"myassignments.html",{'a':a})



@login_required
def edit(request,p):
    # user=request.user
    b=Assignment.objects.get(id=p)
    if(request.method=="POST"):
        a=AssignmentForm(request.POST,request.FILES,instance=b)
        a.save()
        return redirect('students:home')
    a=AssignmentForm(instance=b)
    return render(request,'edit.html',{'a':a})

@login_required
def teachersassignment(request):
    user=request.user
    t=Teacher.objects.filter(user=user)
    return render(request,"teachersassignment.html",{'t':t})

@login_required
def deleteassignment(request,p):
    t=Teacher.objects.get(id=p)
    t.delete()
    return teachersassignment(request)
