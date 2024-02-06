# Employee Management Project #

### This project is a Django-based employee management system consisting of two Django apps: employee and attendance.


**Running the Project**

To run the Django app locally, follow these steps:
1. Clone the repository
2. Navigate to project directory **employee_management**
3. Run django server:  **python manage.py runserver**

## Employee App (Task:1): ##

The employee app provides functionality to manage employee records. It supports creating, updating, deleting, and listing employee records through a RESTful API.
All HTTP requests are therefore made through Postman to the given API endpoints

Endpoints:
To add a new employee: **POST**  http://127.0.0.1:8000/api/employees/

**Example request body:**

**{
    "employee_code": "E002",
    "first_name": "Naeem",
    "last_name": "Niyas",
    "hire_date": "2024-03-06"
}**


To list all employees: **GET** http://127.0.0.1:8000/api/employees/

To retrieve, update, or delete a specific employee:

* **GET**  http://127.0.0.1:8000/api/employees/<employee_code>/

* **PATCH**  http://127.0.0.1:8000/api/employees/<employee_code>/

* **DELETE**  http://127.0.0.1:8000/api/employees/<employee_code>/

## Attendance App (Task:2) 

The attendance app allows tracking employee attendance by recording punch times. Each punch time is associated with an employee and a date, ensuring that the punch time is unique for each employee on a given day.

**Endpoint:**

To add a new punch time: **POST**  http://127.0.0.1:8000/api/attendance/add/

**Example request body:**

**{
    "employee_code": "E002",
    "punch_time": "2024-02-06T12:30:00Z",
    "date": "2024-02-06"
}**

## Task 3 Implementation:

I attempted to implement Task 3, which involves creating a Celery task to automatically generate punch records for employees who have two punch times on the same day. This task aims to capture the first_punch_time and last_punch_time for each employee on a given day and store this information in a separate table named PunchRecord. However, I encountered difficulties and was unable to get it working properly. The code for Task 3 can be found in **attendance/tasks.py**.

## Database

This project uses SQLite as its database backend. All data, including employee records and attendance information, is stored in the SQLite database.
