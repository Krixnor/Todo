from django.urls import path
# from .views import TodoListView,TodoUpdateView
#TodoUpdateView, TodoCreateView
from . import views


urlpatterns = [
    path('task', views.dash, name='task-list'),
    path('all',views.tasks, name='all-list'),
    path('taskUpdate/<int:pk>/', views.task_detail, name='update'),
    # path('task/new/', TodoCreateView.as_view(), name='create'),
    
]