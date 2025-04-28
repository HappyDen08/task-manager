from django import forms
from django.db.models import Q
from django.utils import timezone

from task.models import Task, Worker


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["assignees"].queryset = Worker.objects.filter(
            first_name__isnull=False,
            last_name__isnull=False,
            username__isnull=False
        ).exclude(
            Q(first_name__regex=r"^\s*$") |
            Q(last_name__regex=r"^\s*$") |
            Q(username__regex=r"^\s*$")
        )

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline:
            today = timezone.now().date()
            if deadline < today:
                raise forms.ValidationError("Date can't be in a past")
        return deadline
