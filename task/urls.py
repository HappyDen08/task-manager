from django.urls import path

from .views import Home, TaskDetail, TaskCreate, TaskUpdate, TaskDelete


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task_detail"),
    path("task/create/", TaskCreate.as_view(), name="task_create"),
    path("task/<int:pk>/update/", TaskUpdate.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", TaskDelete.as_view(), name="task_delete")
]

app_name = "task"
