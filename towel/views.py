from rest_framework import status
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
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
def student_detail(request, pk):
    try:
        student = Student.objects.get(id=pk, is_deleted=False)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except:
        return Response('No Records Found', status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_student(request, pk):
    try:
        student = Student.objects.get(id=pk, is_deleted=False)
        serializer = StudentSerializer(student, data=request.data)
        if request.method == 'PUT':
            if serializer.is_valid():
                serializer.save()
                return Response(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response('No Records found', status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student.objects.get(id=pk, is_deleted=False)
        student.is_deleted = True
        student.save()
        return Response('Student deleted successfully!')
    except:
        return Response('No records found!')

