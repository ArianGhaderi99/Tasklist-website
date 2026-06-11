from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('add/', views.TaskCreateView.as_view(), name='task_add'),
    path('<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/toggle/', views.TaskToggleView.as_view(), name='task_toggle'),
]