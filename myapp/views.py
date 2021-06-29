from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Employees, Ragbat
from .serializers import EmployeesSerializer, RagbatSerializer


# boshliq uchun

@api_view(['GET', 'POST'])
def Employes_post(request):
    if request.method == 'GET':
        hodim = Employees.objects.all()
        serializer: EmployeesSerializer = EmployeesSerializer(hodim, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Employes_detail(request, pk):
    try:
        Employeess = Employees.objects.get(pk=pk)
    except Employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeesSerializer(Employeess)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeesSerializer(Employeess, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Employeess.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Rag'batlantrishlar uchun

@api_view(['GET', 'POST'])
def Ragbat_list(request):
    if request.method == 'GET':
        ragbat = Ragbat.objects.all()
        serializer = RagbatSerializer(ragbat, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RagbatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Ragbat_detail(request, pk):
    try:
        Ragbats = Ragbat.objects.get(pk=pk)
    except Ragbats.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RagbatSerializer(Ragbats)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RagbatSerializer(Ragbats, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Ragbats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
