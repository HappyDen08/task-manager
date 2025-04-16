from django.template.context_processors import request
from django.urls import reverse_lazy, reverse

from .models import (
    Task,
    TaskType,
    Worker,
    Position
)

from django.shortcuts import render, get_object_or_404
from django.views import generic


class HomeView(generic.ListView):
    model = Task
    context_object_name = "home"
    template_name = "task/home.html"
    paginate_by = 5

    def get_queryset(self):
        username = self.request.user.username
        return Task.objects.filter(assignees__username=username)


class TaskListView(generic.ListView):
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


class WorkersListView(generic.ListView):
    model = Worker
    context_object_name = "workers_list"
    template_name = "task/workers_list.html"
    paginate_by = 10


class WorkersDetailView(generic.DetailView):
    model = Worker
    context_object_name = "workers_detail"
    template_name = "task/workers_detail.html"


class WorkersUpdateView(generic.UpdateView):
    model = Worker
    context_object_name = "worker_update"
    template_name = "task/workers_update.html"
    fields = ["username", "first_name", "last_name", "email", "position"]
    def get_success_url(self):
        return reverse("task:worker_detail", kwargs={"pk": self.object.pk})



class WorkersDeleteView(generic.DeleteView):
    model = Worker
    context_object_name = "workers_delete"
    template_name = "task/workers_confirm_delete.html"
    success_url = reverse_lazy("task:home")

