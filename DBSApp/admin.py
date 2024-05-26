from django.contrib import admin
from .models import Budget,Employee,HR,ResearchPaper

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('empid','name','department','role','hrid')
admin.site.register(Budget)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ResearchPaper)
admin.site.register(HR)