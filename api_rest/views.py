# Note: Rest API can be used to carry out same operation


from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from dashboard.models import Todo
from .serializers import TaskSerializer
from django.core.paginator import Paginator

# Create your views here.
@login_required
@api_view(['GET','POST'])
def taskList(request):
    if request.method == 'GET':
        tasks = Todo.objects.filter(user=request.user).order_by('-date_posted')
        paginate_by = 2
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        data['user'] = request.user.id
        print(request.data)
        
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','POST','DELETE'])
def task_detail(request,id):
    try:
        task = Todo.objects.get(pk=id,user=request.user)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskSerializer(task) 
        return Response(serializer.data)
        pass
    if request.method == 'POST':
         data = request.body
         data['user'] = request.user.id
         serializer = TaskSerializer(task, data=data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        pass
    pass