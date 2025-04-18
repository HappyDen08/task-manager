from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.views import generic, View

from task.forms import TaskForm
from task.models import (
    Task,
    Worker
)


class HomeView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "home"
    template_name = "task/home.html"
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(assignees=user).annotate(
            total_assignees=Count("assignees")
        ).filter(total_assignees=1).order_by("deadline")

        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query)
            )
        return queryset


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task/task_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = Task.objects.annotate(
            total_assignees=Count("assignees")).filter(
            total_assignees__gte=2).order_by("deadline")
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(assignees__first_name__icontains=query)
            )
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    context_object_name = "task_detail"
    template_name = "task/task_detail.html"


class TaskMyselfDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    context_object_name = "task_myself_detail"
    template_name = "task/task_myself_detail.html"


class TaskCreateMyselfView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ["name",
              "description",
              "deadline",
              "task_type",
              "is_completed",
              "priority"]
    context_object_name = "task_myself_create"
    template_name = "task/task_myself_create.html"
    success_url = reverse_lazy("task:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        # додаємо поточного користувача як виконавця
        self.object.assignees.set([self.request.user])
        return response


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    context_object_name = "task_create"
    template_name = "task/task_create.html"
    success_url = reverse_lazy("task:task_list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    context_object_name = "task_update"
    template_name = "task/task_update.html"

    def get_success_url(self):
        return reverse("task:task_detail", kwargs={"pk": self.object.pk})


class TaskMyselfUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = ["name",
              "description",
              "deadline",
              "task_type",
              "is_completed",
              "priority"]
    context_object_name = "task_myself_update"
    template_name = "task/task_myself_update.html"

    def get_success_url(self):
        return reverse(
            "task:task_myself_detail",
            kwargs={"pk": self.object.pk}
        )


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    context_object_name = "task_delete"
    template_name = "task/task_confirm_delete.html"
    success_url = reverse_lazy("task:home")


class WorkersListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "workers_list"
    template_name = "task/workers_list.html"
    paginate_by = 10


class ToggleDoneView(LoginRequiredMixin, View):

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()
        return redirect(request.META.get("HTTP_REFERER", "/"))
