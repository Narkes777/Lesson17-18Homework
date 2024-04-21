from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/students/', views.students_by_course, name='students_by_course'),
]
