from rest_framework import serializers
from .models import Student, Teacher


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

    def validate_mobile_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Mobile number must contain digits only."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Mobile number must be exactly 10 digits."
            )

        return value


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'