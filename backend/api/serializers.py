from rest_framework import serializers
from .models import TrackedUser, Task, GalleryAlbum, Photo, Post, Comment

class TrackedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackedUser
        fields = ['id', 'name', 'email', 'tel', 'konum', 'company', 'web', 'url', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'kulanici', 'title', 'is_Done', 'created_at']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'album', 'image_url', 'title']


class GalleryAlbumSerializer(serializers.ModelSerializer):
    sample_photos = serializers.SerializerMethodField()
    photos_count = serializers.IntegerField(source='photos.count', read_only=True)
    class Meta:
        model = GalleryAlbum
        fields = ['id', 'owner', 'name', 'sample_photos', 'photos_count', 'created_at']

    
    def get_sample_photos(self, obj):
        photos = obj.photos.all()[:4]
        return [p.image_url for p in photos]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'kulanici', 'title', 'content', 'created_at']
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author_name', 'author_avatar', 'text', 'created_at']
