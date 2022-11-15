from rest_framework.response import Response
from .models import Employees,Departments,Manager,Projects
from .serializers import EmployeesSerializer,DepartmentsSerializer,ManagerSerializer,ProjectsSerializer
from rest_framework import viewsets

class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        Emp= Employees.objects.all()
        Emp_serializer= EmployeesSerializer(Emp, many=True)
        return Response(Emp_serializer.data)

    def create(self, request):
        Emp_serializer= EmployeesSerializer(data= request.data)
        if Emp_serializer.is_valid():
            Emp_serializer.save()
            return Response("Data Created")
        return Response("Error in Creating")

    def update(self,request,pk):
        id=pk
        Emp= Employees.objects.get(pk=id)
        Emp_serializer=EmployeesSerializer(Emp, data=request.data)
        if Emp_serializer.is_valid():
            Emp_serializer.save()
            return Response("Data Updated")
        return Response("Updation failed")

    def destroy(self,request,pk):
        id=pk
        Emp=Employees.objects.get(pk=id)
        Emp.delete
        return Response("Deleted Successfully")

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            Emp=Employees.objects.get(pk=id)
            Emp_serializer = EmployeesSerializer(Emp)
            return Response(Emp_serializer.data)

#Department table viewset

class DepartmentViewSet(viewsets.ViewSet):
    def list(self, request):
        Dep= Departments.objects.all()
        Dep_serializer= DepartmentsSerializer(Dep, many=True)
        return Response(Dep_serializer.data)

    def create(self, request):
        Dep_serializer= DepartmentsSerializer(data= request.data)
        if Dep_serializer.is_valid():
            Dep_serializer.save()
            return Response("Data Created")
        return Response("Error in Creating")

    def update(self,request,pk):
        id=pk
        Dep= Departments.objects.get(pk=id)
        Dep_serializer=DepartmentsSerializer(Dep, data=request.data)
        if Dep_serializer.is_valid():
           Dep_serializer.save()
           return Response("Data Updated")
        return Response("Updation failed")

    def destroy(self,request,pk):
        id=pk
        Dep=Departments.objects.get(pk=id)
        Dep.delete
        return Response("Deleted Successfully")

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
           Dep=Departments.objects.get(pk=id)
           Dep_serializer = DepartmentsSerializer(Dep)
           return Response(Dep_serializer.data)


#Project Model ViewSet
class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset= Projects.objects.all()
    serializer_class= ProjectsSerializer

#Manager Model Viewset
class ManagerModelViewSet(viewsets.ModelViewSet):
    queryset= Manager.objects.all()
    serializer_class= ManagerSerializer
