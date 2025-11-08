from django.shortcuts import render
from rest_framework import viewsets
from .models import TrackedUser, Task, GalleryAlbum, Photo, Post, Comment
from .serializers import TrackedUserSerializer, TaskSerializer, GalleryAlbumSerializer, PhotoSerializer, PostSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class TrackedUserViewSet(viewsets.ModelViewSet):
    queryset = TrackedUser.objects.all().order_by('-created_at')
    serializer_class = TrackedUserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('created_at')
    serializer_class = TaskSerializer


    def get_queryset(self):
        superq = super(). get_queryset()
        user_id = self.request.query_params.get('user')
        if(user_id):
            superq = superq.filter(kulanici_id = user_id)
           
        return  superq
    
    @action(detail=True, methods=["post"])
    def toggle_done(self, request, pk=None):

        task = self.get_object()
        task.is_Done = not task.is_Done

        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class GalleryAlbumViewSet(viewsets.ModelViewSet):
    queryset = GalleryAlbum.objects.all().order_by('created_at')
    serializer_class = GalleryAlbumSerializer


    def get_queryset(self):
        querysuper = super().get_queryset()
        user_id = self.request.query_params.get('user')

        if(user_id):
            querysuper = querysuper.filter(owner_id = user_id)
        
        return querysuper
    

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_queryset(self):
        querysuper = super().get_queryset()
        album = self.request.query_params.get('album')

        if(album):
            querysuper = querysuper.filter(album_id = album)

        return querysuper

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('created_at')
    serializer_class = PostSerializer

    def get_queryset(self):
        querysuper = super().get_queryset()
        user_id = self.request.query_params.get('user')
        if(user_id):
            querysuper = querysuper.filter(kulanici_id = user_id)
        
        return querysuper

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('created_at')
    serializer_class = CommentSerializer

    def get_queryset(self):
        querySuper = super().get_queryset()
        post_id = self.request.query_params.get('post')

        if(post_id):
            querySuper = querySuper.filter(post_id = post_id)
        
        return querySuper

      
          
        
            
        
            
        
            
        



