from django.http import HttpResponse
from django.shortcuts import render
from DBSApp.models import Employee,ResearchPaper
def home(request):
    return render(request, 'home.html')
def hr(request):
    return render(request,'hr.html')
def cld(request):
    empdata=Employee.objects.filter(department='Cloud')
    empcontext={
        'empdata':empdata,
    }
    return render(request,'cld.html',empcontext)
def emp(request):
    empdata=Employee.objects.all()
    empcontext={
        'empdata':empdata,
    }
    return render(request,'emp.html',empcontext)
def rnd(request):
    rnddata=ResearchPaper.objects.all()
    rndcontext={
        'rnddata':rnddata,
    }
    return render(request,'rnd.html',rndcontext)
