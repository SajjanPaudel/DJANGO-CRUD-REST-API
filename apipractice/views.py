from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from .forms import AddForm

""" ---------------------------------------------------------------------------------------
This function returns a dictionary of API endpoints for a task list, detail view, create, update,
and delete.

:param request: The request parameter is an object that contains information about the current
request, such as the HTTP method used, any data submitted with the request, and the user making the
request (if authenticated). It is passed to the view function as an argument
:return: The function `api_home` returns a dictionary of API endpoints with their corresponding URLs
as values. This is returned as a response object using the `Response` class from the Django REST
framework.
-----------------------------------------------------------------------------------------------""" 

@api_view(['GET'])
def api_home(request):
    api_urls={
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>',
    }
    return Response(api_urls)


"""
This function retrieves all tasks from the Task model and returns them as serialized data in a
response object.

:param request: The request parameter is an object that represents the HTTP request made by the
client to the server. It contains information such as the HTTP method used (GET, POST, etc.), the
headers, the query parameters, and the request body. In this case, it is used to retrieve a list of
tasks
:return: a response object that contains serialized data of all the tasks in the database.
"""
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many =True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,id):
    tasks = Task.objects.get(id=id)
    serializer = TaskSerializer(tasks,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request,id):
    task= Task.objects.get(id=id)
    task.delete()
    return redirect('task-list')