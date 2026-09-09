from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Teacher, Course, Student
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer


# API para listar docentes
class TeacherListAPIView(ListAPIView):
    queryset = Teacher.objects.all().order_by('id')
    serializer_class = TeacherSerializer


# API para listar cursos
class CourseListAPIView(ListAPIView):
    queryset = Course.objects.select_related('teacher').all().order_by('id')
    serializer_class = CourseSerializer


# API para listar estudiantes
class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer


# Vista principal
def home(request):
    return render(request, 'academic/base.html')


# Vista para cursos
def courses_page(request):
    return render(request, 'academic/courses.html')


# Vista para estudiantes
def students_page(request):
    return render(request, 'academic/students.html')
