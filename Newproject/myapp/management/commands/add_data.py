from django.core.management.base import BaseCommand
from myapp.models import Student, Course

class Command(BaseCommand):
    help = 'Adds three students and three courses to the database'

    def handle(self, *args, **kwargs):
        # Создаем три курса
        courses = []
        for i in range(1, 4):
            course = Course.objects.create(name=f'Course {i}')
            courses.append(course)
            self.stdout.write(self.style.SUCCESS(f'Course {i} created successfully'))

        # Создаем три студента и привязываем их к курсам
        students_data = [
            {'name': 'Student 1', 'course': courses[0]},
            {'name': 'Student 2', 'course': courses[1]},
            {'name': 'Student 3', 'course': courses[2]},
        ]
        for data in students_data:
            student = Student.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'Student {student.name} created successfully'))
