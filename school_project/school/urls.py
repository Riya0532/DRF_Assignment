from django.urls import path
from .views import (
    StudentCreateAPIView,
    StudentDetailAPIView,
    TeacherListAPIView,
    TeacherUpdateAPIView
)

urlpatterns = [
    path(
        'students/',
        StudentCreateAPIView.as_view(),
        name='student-create'
    ),

    path(
        'students/<int:pk>/',
        StudentDetailAPIView.as_view(),
        name='student-detail'
    ),

    path(
        'teachers/',
        TeacherListAPIView.as_view(),
        name='teacher-list'
    ),

    path(
        'teachers/<int:pk>/',
        TeacherUpdateAPIView.as_view(),
        name='teacher-update'
    ),
]