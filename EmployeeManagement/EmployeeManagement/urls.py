"""EmployeeManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from EmployeeApp import views
from rest_framework.routers import DefaultRouter

#creating router object
router= DefaultRouter()

#Register EmployeeViewSet with router
router.register('EmployeeApi', views.EmployeeModelViewSet, basename='Employee')

#Register EmployeeViewSet with router
router.register('DepartmentApi', views.DepartmentModelViewSet, basename='Department')

#Register ProjectModelViewSet
router.register('ProjectApi', views.ProjectModelViewSet, basename='Project')

#Register ManagerModelViewSet
router.register('ManagerApi', views.ManagerModelViewSet, basename='Project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee', include(router.urls)),
    

]
