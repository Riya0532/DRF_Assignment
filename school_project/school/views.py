from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer


class StudentCreateAPIView(APIView):

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Student added successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class StudentDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return None

    def get(self, request, pk):
        student = self.get_object(pk)

        if not student:
            return Response(
                {"error": "Student not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)

        if not student:
            return Response(
                {"error": "Student not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Student updated successfully",
                    "data": serializer.data
                }
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class TeacherListAPIView(APIView):

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(
            teachers,
            many=True
        )
        return Response(serializer.data)


class TeacherUpdateAPIView(APIView):

    def put(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response(
                {"error": "Teacher not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TeacherSerializer(
            teacher,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Teacher updated successfully",
                    "data": serializer.data
                }
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )