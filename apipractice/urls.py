import requests
from django.urls import path
from .views import api_home,taskList,taskDetail,taskCreate,taskUpdate,taskDelete

urlpatterns = [
    path("",api_home,name="api-home"),
    path("task",taskList,name="task-list"),
    path("task-detail/<str:id>/",taskDetail, name="task-detail"),
    path("task-create/",taskCreate, name="task-create"),
    path("task-update/<str:id>",taskUpdate, name="task-update"),
    path("task-delete/<str:id>",taskDelete, name="task-delete")
]


