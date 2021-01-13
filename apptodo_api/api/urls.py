from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name="api_overview"),
    path('task-list', views.taskList, name="task_list"),
    path('task-detail/<str:pk>',views.taskDetail, name="task_detail"),
    path('task-create', views.taskCreate, name="task_create"),
    path('task-delete/<str:pk>', views.taskDelete, name="task_delete"),
    path('task-update/<str:pk>', views.taskUpdate, name="task_update"),
]