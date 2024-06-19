from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render
from django.views.generic import (
    ListView,DetailView,CreateView, UpdateView, DeleteView)
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@login_required
def dash(request):
    return render(request,'dashboard/task.html')
    pass


def tasks(request):
    if request.method == 'GET':
        tasks = Todo.objects.filter(user=request.user).values('id','title').order_by('-date_posted')
        return JsonResponse(list(tasks),safe=False)
    if request.method == 'POST':
            #loads string from data gotten from client side 
            data = json.loads(request.body)
            #get title and assign to a variable
            title = data.get('title')
            try:
                #create a new entry
                todo = Todo.objects.create(title=title,user=request.user)
                return JsonResponse({"success":True,"message":"created"})
            except Exception as e:
                return JsonResponse({"error":str(e)})



#for editind and deleting 
def task_detail(request,pk):
        try:
            #get the particular item to be edited
            task = Todo.objects.get(user=request.user,id=pk)
        except FileNotFoundError as f:
             return JsonResponse({'error': str(f)}, status=404)
        if request.method == 'POST':
            try:
                #get newly edited string from the client side and assignto a variable
                data = json.loads(request.body)
                #update the old title with the new one
                task.title = data['title']
                task.save()
                return JsonResponse({'message': 'Todo updated successfully'})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
            
        if request.method == 'DELETE':
             task.delete()
             return JsonResponse(status=204)
        
        else:
            return JsonResponse({'error': 'Bad request'}, status=400)
   

             
        
        
       