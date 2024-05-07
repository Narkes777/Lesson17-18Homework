from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/students/', views.students_in_course, name='students_in_course'),
]
