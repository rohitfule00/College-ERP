from django.urls import path
from . import views

urlpatterns = [
    path('', views.admins_dashboard, name='admins_dashboard'),
    path('students/', views.students, name='admin_students'),
    path('teachers/', views.teachers, name='admin_teachers'),
    path('departments/', views.departments, name='admin_departments'),
    path('courses/', views.courses, name='admin_courses'),
    path('classes/', views.classes, name='admin_classes'),
    path('subjects/', views.subjects, name='admin_subjects'),
    path('attendance/', views.attendance, name='admin_attendance'),
    path('exams/', views.exams, name='admin_exams'),
    path('results/', views.results, name='admin_results'),
    path('fees/', views.fees, name='admin_fees'),
    path('notices', views.notices, name='admin_notices'),
    path('reports/', views.reports, name='admin_reports'),
    path('settings/', views.settings, name='admin_settings'),
]
