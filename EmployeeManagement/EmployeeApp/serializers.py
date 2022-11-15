from rest_framework import serializers
from EmployeeApp.models import Employees,Departments,Projects,Manager

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeName','EmployeeID','Department','DOJ')

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentID','DepartmentName')

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields=('ProjectId','ProjectName','ProjectRating')

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields=('ManagerName','ManagerId','ManagerSalary')