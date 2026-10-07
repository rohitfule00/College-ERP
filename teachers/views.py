from django.shortcuts import render

# Create your views here.
def teachers_dashboard(request):
    return render(request, 'teachers/teachers_dashboard.html')

def profile(request):
    return render(request, 'teachers/profile.html')

def classes(request):
    return render(request, 'teachers/classes.html')

def attendance(request):
    return render(request, 'teachers/attendance.html')

def students(request):
    return render(request, 'teachers/students.html')

def assignments(request):
    return render(request, 'teachers/assignments.html')

def marks(request):
    return render(request, 'teachers/marks.html')

def notices(request):
    return render(request, 'teachers/notices.html')

def timetable(request):
    return render(request, 'teachers/timetable.html')

def messages(request):
    return render(request, 'teachers/messages.html')

def settings(request):
    return render(request, 'teachers/settings.html')