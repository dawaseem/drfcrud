from django.shortcuts import render
from django.http import HttpResponse
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student


# Create your views here.

@api_view(['GET'])
def all_students(request):
    students = Student.objects.filter(is_deleted=False)
    if students:
        serialized = StudentSerializer(students, many=True)
        return Response(serialized.data)
    else:
        return Response("No records found")


@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def student_details(request):
    print('Here...1')
    id = request.data['id']
    student = Student.objects.get(id=id, is_deleted=False)

    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_student(request, pk):
    student = Student.objects.get(id=pk, is_deleted=False)
    student.is_deleted = True
    student.save()
    return Response('Student deleted successfully!')
