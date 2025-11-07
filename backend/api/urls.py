from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrackedUserViewSet, TaskViewSet, GalleryAlbumViewSet, PhotoViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'tracked-users', TrackedUserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'gallery-albums', GalleryAlbumViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls
