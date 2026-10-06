from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('courses/', views.courses, name='courses'),
    path('attendance/', views.attendance, name='attendance'),
    path('timetable/', views.timetable, name='timetable'),
    path('assignment/', views.assignment, name='assignment'),
    path('result/', views.result, name='result'),
    path('fees/', views.fees, name='fees'),
    path('announcements', views.announcements, name='announcements'),
    path('settings/', views.settings, name='settings')
]