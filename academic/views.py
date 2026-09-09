from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Teacher, Course, Student
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer


class TeacherListAPIView(ListAPIView):
    queryset = Teacher.objects.all().order_by('id')
    serializer_class = TeacherSerializer


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.select_related('teacher').all().order_by('id')
    serializer_class = CourseSerializer


class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer


def home(request):
    return render(request, 'academic/base.html')


def courses_page(request):
    return render(request, 'academic/courses.html')


def students_page(request):
    return render(request, 'academic/students.html')
