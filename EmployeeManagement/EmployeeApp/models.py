from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# 4 models are given to us


# EmployeeModel
class Employees(models.Model):
    EmployeeName=models.CharField(max_length=500)
    EmployeeID=models.AutoField(primary_key=True)
    Department=models.CharField(max_length=500)
    DOJ=models.DateField()


#DepartmentModel
class Departments(models.Model):
    DepartmentID=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=500)


#ProjectModel
class Projects(models.Model):
    ProjectId=models.AutoField(primary_key=True)
    ProjectName=models.CharField(max_length=500)
    ProjectRating=models.IntegerField()


# ManagerModel
class Manager(models.Model):
    ManagerName= models.CharField(max_length=500)
    ManageId= models.AutoField(primary_key=True)
    ManagerSalary= models.IntegerField()
    
    





