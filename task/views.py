from django.urls import reverse_lazy, reverse

from .models import (
    Task,
    TaskType,
    Worker,
    Position
)

from django.shortcuts import render
from django.views import generic


class HomeView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task/task_list.html"
    paginate_by = 5


class TaskDetailView(generic.DetailView):
    model = Task
    context_object_name = "task_detail"
    template_name = "task/task_detail.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    context_object_name = "task_create"
    template_name = "task/task_create.html"
    success_url = reverse_lazy("task:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    context_object_name = "task_update"
    template_name = "task/task_update.html"
    def get_success_url(self):
        return reverse("task:task_detail", kwargs={"pk": self.object.pk})


class TaskDeleteView(generic.DeleteView):
    model = Task
    context_object_name = "task_delete"
    template_name = "task/task_confirm_delete.html"
    success_url = reverse_lazy("task:home")


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = ("task/worker_list.html")
    paginate_by = 10
