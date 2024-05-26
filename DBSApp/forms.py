from django import forms
from .models import Employee,ResearchPaper

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['empid', 'name', 'department', 'role', 'hrid']
class rndForm(forms.ModelForm):
    class Meta:
        model = ResearchPaper
        fields = ['project_id', 'project_name', 'Research_Papers', 'conference', 'funding','empid']
        