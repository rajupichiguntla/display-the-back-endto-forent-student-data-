from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
'''def htmlform(request):
    
    return render(request,'htmlform.html')'''

def insert_School(request):
    if request.method=='POST':
        scn=request.POST['scn']#name  attributes values
        sp=request.POST['sp']
        sl=request.POST['sl']
        
        
        
        SO=School.objects.get_or_create(scname=scn,scprincipal=sp,sclocation=sl)[0]
        SO.save()

        QLSO=School.objects.all()
        d={'QLSO':QLSO}
        return render(request,'display_school.html',d)
    
    return render(request,'insert_school.html')


def insert_Student(request):
    if request.method=='POST':
        scn=request.POST['scn']
        sn=request.POST['sn']
        si=request.POST['si']
        
        
        SO=School.objects.get(scname=scn)
        # SO.save()
        STO=Student.objects.get_or_create(scname=SO,sname=sn,sid=si)[0]
        STO.save()
        
       

        QLST=Student.objects.all()
        d={'QLST':QLST}
        return render(request,'display_student.html',d)
    
    return render(request,'insert_student.html')

