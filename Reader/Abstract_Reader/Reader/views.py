from django.shortcuts import render
from django.shortcuts import render,redirect
from Reader.models import Student
from django.contrib.auth.models import User



# Create your views here.
def HOME(request):
    return render (request,'main/base.html')

def STUDENTS(request):
    student=Student.objects.all()
    context={
        'student':student,
    }
    return render(request,'main/student.html',context)


def PROJECT_DETAILS(request,name):
    student=Student.objects.filter(name=name)
    context={
        'student':student,
    }
    return render(request,'main/Project.html',context)

def SEARCH(request):
   rollno=request.GET['rollno']
   student_search=Student.objects.filter(rollno=rollno)

   context={
       'student_search':student_search
       }
   return render(request,'main/search.html',context)

def BATCH(request):
   batch=request.GET['batch']
   student_search=Student.objects.filter(batch=batch)

   context={
       'student_search':student_search
       }
   return render(request,'main/batch.html',context)