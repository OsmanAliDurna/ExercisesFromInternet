from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Todo
from .serializers import TodoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )


@api_view(['GET'])
def todolist(request):

    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def todocreate(request):

    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
