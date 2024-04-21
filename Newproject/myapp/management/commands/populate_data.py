from django.core.management.base import BaseCommand
from myapp.models import Student, Course


class Command(BaseCommand):
    help = 'Populate database with initial data'

    def handle(self, *args, **kwargs):
        # Добавление трех курсов
        Course.objects.create(name='Mathematics')
        Course.objects.create(name='Physics')
        Course.objects.create(name='Chemistry')

        # Добавление трех студентов
        Student.objects.create(name='Alice', course_id=1)
        Student.objects.create(name='Bob', course_id=2)
        Student.objects.create(name='Charlie', course_id=3)

        self.stdout.write(self.style.SUCCESS(
            'Data has been successfully populated!'))
