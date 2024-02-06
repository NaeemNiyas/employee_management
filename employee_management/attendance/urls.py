from django.urls import path
from .views import AttendanceCreateView

urlpatterns = [
    path('add/', AttendanceCreateView.as_view(), name='add_attendance'),
]
