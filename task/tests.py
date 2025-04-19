from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from task.models import Task, TaskType, Position

User = get_user_model()


class ModelTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.task_type = TaskType.objects.create(name="Bug")
        self.worker = get_user_model().objects.create_user(
            username="johndoe",
            password="testpass123",
            first_name="John",
            last_name="Doe",
            position=self.position
        )

    def test_worker_str(self):
        self.assertEqual(str(self.worker), "John Doe (johndoe)")

    def test_position_str(self):
        self.assertEqual(str(self.position), "Developer")

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), "Bug")

    def test_create_task(self):
        task = Task.objects.create(
            name="Fix login bug",
            description="User cannot login with valid credentials",
            deadline=timezone.now().date(),
            is_completed=False,
            priority="High",
            task_type=self.task_type
        )
        task.assignees.add(self.worker)
        self.assertEqual(str(task), "Fix login bug")
        self.assertIn(self.worker, task.assignees.all())


class TaskViewTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.user = User.objects.create_user(
            username="testuser",
            password="password123",
            first_name="Test",
            last_name="User",
            position=self.position
        )
        self.task_type = TaskType.objects.create(name="Bug")
        self.task = Task.objects.create(
            name="Fix login issue",
            description="Fix the user login issue",
            deadline="2025-12-31",
            is_completed=False,
            priority="High",
            task_type=self.task_type
        )
        self.task.assignees.add(self.user)

    def test_home_view_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("task:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fix login issue")

    def test_task_list_view_authenticated(self):
        user2 = User.objects.create_user(username="otheruser", password="pass")
        self.task.assignees.add(user2)
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse("task:task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fix login issue")

    def test_task_detail_view_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.get(
            reverse(
                "task:task_detail",
                args=[self.task.pk]
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.name)

    def test_toggle_done(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(
            reverse(
                "task:toggle_done",
                args=[self.task.pk]
            ),
            follow=True
        )
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_completed)
        self.assertEqual(response.status_code, 200)
