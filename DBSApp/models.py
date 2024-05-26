from django.db import models

# Create your models here.
class HR(models.Model):
    hrid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    Email_address=models.EmailField(max_length=50)
    def __str__(self):
        return self.name

class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    hrid=models.ForeignKey(HR,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name

class Budget(models.Model):
    year=models.IntegerField(primary_key = True)
    revenue = models.FloatField()
    expenditure = models.FloatField()
    profit = models.FloatField()
    def __str__(self):
        return self.year

class ResearchPaper(models.Model):
    project_id=models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=50)
    Research_Papers = models.CharField(max_length=50)
    conference = models.CharField(max_length=50)
    funding =models.FloatField()
    empid=models.ForeignKey(Employee, on_delete=models.SET_NULL,null=True) 
    def __str__(self):
        return self.project_name


