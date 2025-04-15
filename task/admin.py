from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Position,
    TaskType,
    Task,
    Worker
)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    search_fields = ("name", )


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    model = Worker
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "position",
        "is_staff",
        "is_active"
    )
    list_filter = ("position", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("position",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("position",)}),
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email"
    )


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    search_fields = ("name", )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "task_type",
        "deadline",
        "priority",
        "is_completed"
    )
    list_filter = ("priority", "is_completed", "task_type")
    search_fields = ("name", "description")
