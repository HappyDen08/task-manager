from django.db.models import Count
from django.db.models import Q
from django.template.context_processors import request
from django.urls import reverse_lazy, reverse

from .forms import TaskForm
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
        user = self.request.user
        return Task.objects.filter(assignees=user).annotate(
            total_assignees=Count("assignees")
        ).filter(total_assignees=1).order_by("deadline")


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task/task_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.annotate(total_assignees=Count("assignees")).filter(
            total_assignees__gte=2).order_by("deadline")


class TaskDetailView(generic.DetailView):
    model = Task
    context_object_name = "task_detail"
    template_name = "task/task_detail.html"


class TaskCreateMyselfView(generic.CreateView):
    model = Task
    fields = ["name", "description", "deadline", "task_type", "is_completed", "priority"]
    context_object_name = "task_myself_create"
    template_name = "task/task_myself_create.html"
    success_url = reverse_lazy("task:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        # додаємо поточного користувача як виконавця
        self.object.assignees.set([self.request.user])
        return response


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    context_object_name = "task_create"
    template_name = "task/task_create.html"
    success_url = reverse_lazy("task:task_list")



class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
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
