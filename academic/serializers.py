from rest_framework import serializers
from .models import Teacher, Course, Student


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name']


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name']
