from . import views
from django.urls import path

urlpatterns = [
    path('', views.addTasks, name='addTasks'),
    path('details', views.details, name='details'),
    path('delete/<int:taskId>/', views.deleteTask, name='deleteTask'),
    path('update/<int:taskId>/', views.update, name='update'),
    path('cbvHome/', views.TaskListView.as_view(), name='cbvHome'),
    path('cbvDetail/<int:pk>/', views.TaskDetailview.as_view(), name='cbvDetails'),
    path('cbvEdit/<int:pk>/', views.TaskUpdateview.as_view(), name='cbvupdate'),
    path('cbvDelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cbvDeletes'),
]
