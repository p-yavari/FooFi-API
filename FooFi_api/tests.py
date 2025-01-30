"""
Test suite for the FooFi API.

This file was written with assistance from an AI (ChatGPT) to ensure comprehensive API test coverage.

Author: Pooria
"""

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from FooFi_api.models import TaskEntry

class FooFiAPITests(APITestCase):
    """Test suite for the FooFi API."""

    def setUp(self):
        """Set up test user and authentication token."""
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com",
            name="Test User",
            password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        """Test creating a new task."""
        payload = {
            "title": "Sample Task",
            "description": "This is a test task.",
            "due_date": "2024-07-01T12:00:00Z",
            "completed": False
        }
        response = self.client.post("/api/tasks/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], payload["title"])

    def test_get_task_list(self):
        """Test retrieving a list of tasks."""
        TaskEntry.objects.create(user_profile=self.user, title="Task 1", description="Task 1 Desc", due_date="2024-07-01T12:00:00Z", completed=False)
        TaskEntry.objects.create(user_profile=self.user, title="Task 2", description="Task 2 Desc", due_date="2024-07-02T12:00:00Z", completed=True)

        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_task(self):
        """Test updating an existing task."""
        task = TaskEntry.objects.create(user_profile=self.user, title="Old Task", description="Old Desc", due_date="2024-07-01T12:00:00Z", completed=False)
        payload = {"title": "Updated Task", "description": "Updated Desc", "due_date": "2024-07-03T12:00:00Z", "completed": True}

        response = self.client.put(f"/api/tasks/{task.id}/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], payload["title"])

    def test_delete_task(self):
        """Test deleting a task."""
        task = TaskEntry.objects.create(user_profile=self.user, title="Task to Delete", description="Delete me", due_date="2024-07-01T12:00:00Z", completed=False)
        response = self.client.delete(f"/api/tasks/{task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(TaskEntry.objects.filter(id=task.id).exists())

    def test_authentication_required(self):
        """Test that authentication is required for accessing tasks."""
        self.client.force_authenticate(user=None)  # Remove authentication
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
