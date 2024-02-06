from django.db import models

class Employee(models.Model):
    employee_code = models.CharField(max_length=20, primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.employee_code} - {self.first_name} {self.last_name}"

