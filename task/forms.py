from django import forms
from django.db.models import Q

from .models import Task, Worker

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Фільтруємо список працівників
        self.fields["assignees"].queryset = Worker.objects.filter(
            first_name__isnull=False,
            last_name__isnull=False,
            username__isnull=False
        ).exclude(
            Q(first_name__regex=r"^\s*$") |
            Q(last_name__regex=r"^\s*$") |
            Q(username__regex=r"^\s*$")
        )