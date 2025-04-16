from django.urls import path

from .views import Home, TaskDetail, TaskCreate


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task_detail"),
    path("task/create/", TaskCreate.as_view(), name="task_create")
]

app_name = "task"
