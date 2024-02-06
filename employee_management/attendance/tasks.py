from celery import shared_task
from django.db.models import Count
from .models import Attendance, PunchRecord

@shared_task
def create_punch_records():
    # Query Attendance table to find instances where an employee has two punch times on the same day
    attendance_list = Attendance.objects.values('employee_code', 'date').annotate(punch_count=Count('id')).filter(punch_count__gte=2)

    for attendance in attendance_list:
        # Get the employee code and date
        employee_code = attendance['employee_code']
        date = attendance['date']
        
        # Get the first and last punch times for the employee on the same day
        first_punch_time = Attendance.objects.filter(employee_code=employee_code, date=date).order_by('punch_time').first().punch_time
        last_punch_time = Attendance.objects.filter(employee_code=employee_code, date=date).order_by('-punch_time').first().punch_time

        # Create a new PunchRecord
        PunchRecord.objects.create(employee_code=employee_code, first_punch_time=first_punch_time, last_punch_time=last_punch_time)
