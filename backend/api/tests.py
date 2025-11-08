
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import TrackedUser, Task

class TrackedUserTests(APITestCase):
    def setUp(self):
        self.user = TrackedUser.objects.create(name="Test User")

    def test_list_users(self):
        url = reverse('trackeduser-list')  
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(res.data), 1)

    def test_create_task_for_user(self):
        url = reverse('task-list')
        payload = {
            "kulanici": self.user.id,
            "title": "ilk görev"
        }
        res = self.client.post(url, payload, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, "ilk görev")


class TaskActionTests(APITestCase):
    def setUp(self):
        self.user = TrackedUser.objects.create(name="Task Owner")
        self.task = Task.objects.create(kulanici=self.user, title="yapılacak", is_Done=False)

    def test_toggle_done_action(self):
        url = reverse('task-toggle-done', kwargs={'pk': self.task.id})
        res = self.client.post(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_Done)

