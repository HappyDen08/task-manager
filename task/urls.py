from django.urls import path

from task.views import (
    HomeView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskCreateMyselfView,
    TaskMyselfDetailView,
    TaskMyselfUpdateView,
    WorkersListView,
    ToggleDoneView
)


urlpatterns = [
    path(
        "",
        HomeView.as_view(),
        name="home"
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task_list"
    ),
    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task_detail"
    ),
    path(
        "tasks/myself/<int:pk>/",
        TaskMyselfDetailView.as_view(),
        name="task_myself_detail"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task_create"
    ),
    path(
        "tasks/myself/create",
        TaskCreateMyselfView.as_view(),
        name="task_myself_create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task_update"
    ),
    path(
        "tasks/<int:pk>/myself/update/",
        TaskMyselfUpdateView.as_view(),
        name="task_myself_update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task_delete"
    ),
    path(
        "workers/",
        WorkersListView.as_view(),
        name="workers_list"
    ),
    path(
        "tasks/<int:pk>/toggle_done/",
        ToggleDoneView.as_view(),
        name="toggle_done"
    ),
]

app_name = "task"
