from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses_page, name='courses_page'),
    path('students/', views.students_page, name='students_page'),
    path('api/teachers/', views.TeacherListAPIView.as_view(), name='teacher-list'),
    path('api/courses/', views.CourseListAPIView.as_view(), name='course-list'),
    path('api/students/', views.StudentListAPIView.as_view(), name='student-list'),
]
