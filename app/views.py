from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
def fun1(request):
    dno=int(input('enter dept no : '))
    deptno=dept.objects.get_or_create(deptno=dno)[0]
    deptno.save()
    dnao=input('enter a dname : ')
    dlo=input('enter a dloc : ')
    deptob=dept.objects.get_or_create(dname=dnao,dloc=dlo)[0]
    deptob.save()
    return HttpResponse('data inserted')

def fun2(request):
    dno=int(input('enter a deptno : '))
    deptno=dept.objects.get_or_create(deptno=dno)[0]
    eno=input('enter e name : ')
    sao=int(input('enter a sal : '))
    job=input('enter a job : ')
    coo=int(input('enter a comm : '))
    empob=emp.objects.get_or_create(deptno=deptno,ename=eno,sal=sao,job=job,comm=coo)[0]
    empob.save()
    return HttpResponse('data inserted')


qsdo=dept.objects.all()
qseo=emp.objects.all()
d={'qsdo':qsdo}
a={'qseo':qseo}
def display_dept(request):
    return render(request,'display_dept.html',context=d)
    return render(request,'display_dept.html',context=a)

