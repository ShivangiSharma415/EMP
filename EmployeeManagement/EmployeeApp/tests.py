from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


URLS = ['DepartmentApi',  'ProjectApi', 'EmployeeApi', 'ManagerApi']


# Create your tests here.
class UserAPITest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_department_successful(self):
        #Arrange
        data = {
            "department_id": "D1",
            "department_name": "Engineer"
        }

        #Act
        result = self.client.post(reverse(URLS[0], data))

        #Assert
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

  

  

    def test_create_project_successful(self):
        #Arrange
        data = {
            "project_id": "P1",
            "project_name": "Library Management System",
            "project_rating": "3",
            
        }

        #Act
        result = self.client.post(reverse(URLS[1], data))

        #Assert
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)



    def test_create_employee_successful(self):
        #Arrange
        data = {
            "employee_id": "100",
            "employee_name": "John",
            "department": "IT",
            "doj": "20-10-22"
        }

        #Act
        result = self.client.post(reverse(URLS[3], data))

        #Assert
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)


    def test_create_manager_successful(self):
        #Arrange
        data = {
            
            "manger_id": "M1",
            "manager_name": "Kelvin",
            "salary": "50000"
        }

        #Act
        result = self.client.post(reverse(URLS[3], data))

        #Assert
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
