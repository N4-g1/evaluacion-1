from django.test import TestCase
from django.urls import reverse

from .models import Teacher


class AcademicViewsTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_courses_page_loads(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)

    def test_students_page_loads(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_api_courses_endpoint(self):
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.json())

    def test_api_courses_can_create_course(self):
        teacher = Teacher.objects.create(first_name='Ana', last_name='García')

        response = self.client.post('/api/courses/', {
            'name': 'Física',
            'teacher': teacher.id,
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], 'Física')

    def test_api_students_can_create_student(self):
        response = self.client.post('/api/students/', {
            'first_name': 'Luis',
            'last_name': 'Pérez',
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['first_name'], 'Luis')
