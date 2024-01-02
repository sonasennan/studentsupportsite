from django.shortcuts import render
from django.db.models import Q
from students.models import Notes,Questionpapers
# Create your views here.
def notessearch_result(request):
    query=""
    notesdetails=None
    questionpapers=None
    if(request.method=="POST"):
        query=request.POST['s']
        if(query):
            notesdetails=Notes.objects.filter(Q(subject__icontains=query)|Q(year__icontains=query))
            questionpapers=Questionpapers.objects.filter(Q(subject__icontains=query)|Q(year__icontains=query))

    return render(request,'searchnotes.html',{'n':notesdetails,'q':query,'searchquestionpapers':questionpapers})
