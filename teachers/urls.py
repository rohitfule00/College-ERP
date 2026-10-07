from django.urls import path
from . import views


urlpatterns = [
    path('', views.teachers_dashboard, name='teachers_dashboard'),
    path('profile/', views.profile, name='teacher_profile'),
    path('classes/', views.classes, name='teacher_classes'),
    path('students/', views.students, name='teacher_students'),
    path('attendance/', views.attendance, name='teacher_attendance'),
    path('assignments/', views.assignments, name='teacher_assignments'),
    path('marks/', views.marks, name='teacher_marks'),
    path('notices/', views.notices, name='teacher_notices'),
    path('timetable/', views.timetable, name='teacher_timetable'),
    path('messages/', views.messages, name='teacher_messages'),
    path('settings/', views.settings, name='teacher_settings'),

]
