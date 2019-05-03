from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import AttendanceList, Course, Student, LecturerSession, Unit, UnitAssign, Lecturer

# Create your views here.


class AttendanceList(APIView):
    def get(self, request):
        attendance_details = AttendanceList.objects.all()
        print(attendance_details)
        data = serializers.AttendanceListSerializer(attendance_details, many=True).data
        return Response(data)


def filter(request):
    query = AttendanceList.objects.all().values('adm_no', 'full_name')
    data = list(query)
    return JsonResponse(data, safe=False)