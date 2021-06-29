from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Commands_table
from .serializers import Commands_tableSerializer

@api_view(['GET', 'POST'])
def Comands(request):
    if request.method == 'GET':
        comand = Commands_table.objects.all()
        serializer = Commands_tableSerializer(comand, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Commands_tableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Putcomand(request):
    try:
        Comand = Comands.objects.all()
    except Comand.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = Commands_tableSerializer(Comand)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = Commands_tableSerializer(Comand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Comand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

