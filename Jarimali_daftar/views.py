from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Fines
from .serializers import FinesSerializer

@api_view(['GET', 'POST'])
def fines_list(request):
    if request.method == 'GET':
        fines = Fines.objects.all()
        serializer = FinesSerializer(fines, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def fines_detail(request):
    try:
        fines = Fines.objects.all()
    except fines.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = FinesSerializer(fines)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = FinesSerializer(fines, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fines.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
