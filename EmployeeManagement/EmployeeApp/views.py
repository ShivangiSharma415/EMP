from rest_framework.response import Response
from .models import Employees,Departments,Manager,Projects
from .serializers import EmployeesSerializer,DepartmentsSerializer,ManagerSerializer,ProjectsSerializer
from rest_framework import viewsets

#Employees Model Viewset
class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset=Employees.objects.all()
    serializer_class=EmployeesSerializer


#Departments Model Viewset
class DepartmentModelViewSet(viewsets.ModelViewSet):
    queryset=Departments.objects.all()
    serializer_class=DepartmentsSerializer


#Project Model ViewSet
class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset= Projects.objects.all()
    serializer_class= ProjectsSerializer

#Manager Model Viewset
class ManagerModelViewSet(viewsets.ModelViewSet):
    queryset= Manager.objects.all()
    serializer_class= ManagerSerializer
