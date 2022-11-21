from django.db import models

# Create your models here.
class StudentDetail(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    enrollment_number = models.CharField(max_length=12)
    semester = models.PositiveIntegerField()
    department = models.CharField(max_length=20)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.first_name +" "+ self.last_name

class EmployeeDetail(models.Model):
    employee_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    department = models.CharField(max_length=30)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.first_name +" "+ self.last_name