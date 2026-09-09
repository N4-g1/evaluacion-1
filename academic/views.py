from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .models import Teacher, Course, Student
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer


# API para listar docentes
class TeacherListAPIView(ListAPIView):
    queryset = Teacher.objects.all().order_by('id')
    serializer_class = TeacherSerializer


# API para listar y crear cursos
class CourseListAPIView(ListCreateAPIView):
    queryset = Course.objects.select_related('teacher').all().order_by('id')
    serializer_class = CourseSerializer


# API para listar y crear estudiantes
class StudentListAPIView(ListCreateAPIView):
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
