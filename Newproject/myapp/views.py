from django.shortcuts import render
from .models import Student

def students_in_course(request, course_id):
    students = Student.objects.filter(course_id=course_id)
    return render(request, 'students.html', {'students': students})
