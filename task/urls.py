from django.urls import path

from .views import (
    HomeView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    WorkersListView,
    WorkersDetailView,
    WorkersUpdateView,
    WorkersDeleteView
)


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("task/", TaskListView.as_view(), name="task_list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("workers/", WorkersListView.as_view(), name="workers_list"),
    path("workers/<int:pk>/", WorkersDetailView.as_view(), name="workers_detail"),
    path("workers/<int:pk>/update/", WorkersUpdateView.as_view(), name="workers_update"),
    path("workers/<int:pk>/delete/", WorkersDeleteView.as_view(), name="workers_delete")
]

app_name = "task"
