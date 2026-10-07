from django.shortcuts import render

# Create your views here.

def admins_dashboard(request):
    return render(request, 'admins/admins_dashboard.html')

def students(request):
    return render(request, 'admins/students.html')

def teachers(request):
    return render(request, 'admins/teachers.html')

def departments(request):
    return render(request, 'admins/departments.html')

def courses(request):
    return render(request, 'admins/courses.html')

def classes(request):
    return render(request, 'admins/classes.html')

def subjects(request):
    return render(request, 'admins/subjects.html')

def attendance(request):
    return render(request, 'admins/attendance.html')

def exams(request):
    return render(request, 'admins/exams.html')

def results(request):
    return render(request, 'admins/results.html')

def fees(request):
    return render(request, 'admins/fees.html')

def notices(request):
    return render(request, 'admins/notices.html')

def reports(request):
    return render(request, 'admins/reports.html')

def settings(request):
    return render(request, 'admins/settings.html')