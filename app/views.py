from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from models import Student
from serializers import StudentSerializer


@api_view(['GET', 'POST'])
def student_collection(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = {'first_name': request.DATA.get('first_name'),
                'last_name': request.DATA.data('last_name'),
                'date_of_birth': request.DATA.data('date_of_birth'),
                'grade': request.DATA.data('grade'),
                'phone': request.DATA.data('phone'),
                'email': request.DATA.data('email')}
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def student_record(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
