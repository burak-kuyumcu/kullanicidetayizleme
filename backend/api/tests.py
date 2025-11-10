
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import TrackedUser, Task, GalleryAlbum, Photo, Post, Comment

class TrackedUserTests(APITestCase):
    def setUp(self):
        self.user = TrackedUser.objects.create(
            name="Test User",
            email="test@example.com",
            company="testCompany",
        )

    def test_list_users(self):

        url = reverse('trackeduser-list')  
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
        self.assertGreaterEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["name"], "Test User")

    def test_create_user(self):

        url = reverse('trackeduser-list')

        payload = { "name": "Yeni Kullanıcı", "email": "yeni@example.com",}

        res = self.client.post(url, payload, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue( TrackedUser.objects.filter(name="Yeni Kullanıcı").exists())


class TaskTests(APITestCase):

    def setUp(self):

        self.user = TrackedUser.objects.create(name="Task Owner")
        self.task = Task.objects.create(kulanici=self.user, title="ilk görev", is_Done=False,)

    def test_list_tasks_filter_by_user(self):

        other = TrackedUser.objects.create(name="Other")
        Task.objects.create(kulanici=other, title="başka")
        url = reverse('task-list')
        res = self.client.get(url, {"user": self.user.id})


        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

        self.assertEqual(res.data[0]["title"], "ilk görev")


    def test_create_task_for_user(self):

        url = reverse('task-list')
        payload = {"kulanici": self.user.id,"title": "ikinci görev"}
        res = self.client.post(url, payload, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.latest("id").title, "ikinci görev")


    def test_toggle_done_action(self):
       
        url = reverse('task-toggle-done', kwargs={'pk': self.task.id})
        res = self.client.post(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_Done)


class GalleryTests(APITestCase):
    def setUp(self):
        self.user = TrackedUser.objects.create(name="Gallery Owner")
        self.album = GalleryAlbum.objects.create(owner=self.user,name="Tatil")
      
        Photo.objects.create(album=self.album, image_url="https://img/1.jpg", title="1")
        Photo.objects.create(album=self.album, image_url="https://img/2.jpg", title="2")
        Photo.objects.create(album=self.album, image_url="https://img/3.jpg", title="3")

    def test_list_albums_of_user(self):

        url = reverse('galleryalbum-list')
        res = self.client.get(url, {"user": self.user.id})


        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data[0]["name"], "Tatil")
        self.assertIn("sample_photos", res.data[0])
        self.assertEqual(len(res.data[0]["sample_photos"]), 3)

    def test_list_photos_of_album(self):
        url = reverse('photo-list')
        res = self.client.get(url, {"album": self.album.id})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 3)
        self.assertEqual(res.data[0]["album"], self.album.id)


class PostCommentTests(APITestCase):

    def setUp(self):

        self.user = TrackedUser.objects.create(name="Poster")
        self.post = Post.objects.create(kulanici=self.user,title="ilk post",content="Bu bir test Postudur")
        self.comment = Comment.objects.create(post=self.post,author_name="Ali",text="güzel olmuş")

    def test_list_posts_of_user(self):

        url = reverse('post-list')
        res = self.client.get(url, {"user": self.user.id})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["title"], "ilk post")

    def test_create_comment_for_post(self):

        url = reverse('comment-list')
        payload = {"post": self.post.id,"author_name": "Veli","text": "ben de beğendim",}
        res = self.client.post(url, payload, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.post.comments.count(), 2)


