from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('create/', TaskCreateView.as_view(), name='create'),
]