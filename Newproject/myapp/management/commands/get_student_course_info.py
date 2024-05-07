from django.core.management.base import BaseCommand
from myapp.models import Student, Course


class Command(BaseCommand):
    help = 'Displays list of courses for each student and list of students for each course'

    def handle(self, *args, **options):

        students = Student.objects.all()
        for student in students:
            print(student.name)
            for course in student.courses.all():
                print(course)
