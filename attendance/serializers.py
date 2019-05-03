from rest_framework import serializers
from . import models


class AttendanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AttendanceList
        fields = '__all__'


class LecturerSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LecturerSession
        fields = '__all__'
