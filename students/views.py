from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'students/dashboard.html')

def profile(request):
    return render(request, 'students/profile.html')

def courses(request):
    return render(request, 'students/courses.html')

def attendance(request):
    return render(request, 'students/attendance.html')

def timetable(request):
    return render(request, 'students/timetable.html')

def assignment(request):
    return render(request, 'students/assignment.html')

def result(request):
    return render(request, 'students/result.html')

def fees(request):
    return render(request, 'students/fees.html')

def announcements(request):
    return render(request, 'students/announcements.html')

def settings(request):
    return render(request, 'students/settings.html')