from django.shortcuts import render
from .models import Course

# Create your views here.


def students_by_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    students = course.student_set.all()
    return render(request, 'students_by_course.html', {'students': students})
