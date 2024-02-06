from django.db import models
from employee.models import Employee

class Attendance(models.Model):
    employee_code = models.ForeignKey(Employee, on_delete=models.CASCADE, to_field='employee_code')
    punch_time = models.DateTimeField()   # Stores the time when an employee punches in
    date = models.DateField()   # Stores the date of the punch
    class Meta:
        unique_together = ['employee_code', 'date', 'punch_time']   # Ensures each punch record is unique based on employee, date, and time

    def __str__(self):
        return f"{self.employee_code.employee_code} - {self.punch_time} - {self.date}"

class PunchRecord(models.Model):
    employee_code = models.ForeignKey(Employee, on_delete=models.CASCADE)
    first_punch_time = models.DateTimeField()
    last_punch_time = models.DateTimeField()

    def __str__(self):
        return f"{self.employee_code.employee_code} - {self.first_punch_time} - {self.last_punch_time}"