from .models import (
    Task,
    TaskType,
    Worker,
    Position
)

from django.shortcuts import render
from django.views import generic


class Home(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task/task_list.html"
    paginate_by = 5


class TaskDetail(generic.DetailView):
    model = Task
    context_object_name = "task_detail"
    template_name = "task/task_detail.html"