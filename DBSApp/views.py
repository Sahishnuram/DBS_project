from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .forms import EmployeeForm,rndForm
from .models import Employee,ResearchPaper
# Create your views here.
def addEmployee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Employee has been added successfully!')
    else:
        form = EmployeeForm()
    return render(request, 'addEmployee.html', {'form': form})
def addrnd(request):
    if request.method == "POST":
        form = rndForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('R & D has been added successfully!')
    else:
        form = rndForm()
    return render(request, 'addrnd.html', {'form': form})
def delemployee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')
def employee_list(request):
    empdata=Employee.objects.all()
    empcontext={
        'empdata':empdata,
    }
    return render(request,'employee_list.html',empcontext)
def delrnd(request,pk):
    rnd=get_object_or_404(ResearchPaper,pk=pk)
    rnd.delete()
    return redirect('rnd_list')
def rnd_list(request):
    rnddata=ResearchPaper.objects.all()
    rndcontext={
        'rnddata':rnddata,
    }
    return render(request,'rnd_list.html',rndcontext)

