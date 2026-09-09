from rest_framework import serializers
from .models import Teacher, Course, Student


# Serializador para docentes
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name']


# Serializador para cursos con información del docente
class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        source='teacher',
        queryset=Teacher.objects.all(),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'teacher_id']

    def to_internal_value(self, data):
        data = data.copy()
        if 'teacher' in data and 'teacher_id' not in data:
            data['teacher_id'] = data['teacher']
        return super().to_internal_value(data)


# Serializador para estudiantes
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name']
