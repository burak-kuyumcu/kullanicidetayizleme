from django.db import models

class TrackedUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    tel = models.CharField(blank=True, max_length=50, null=True)
    konum = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    web = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    

    def __str__(self):
        return self.name

class Task(models.Model):
    kulanici = models.ForeignKey(TrackedUser, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    is_Done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.name} - {self.title}"

class GalleryAlbum(models.Model):
    
    owner = models.ForeignKey('api.TrackedUser', related_name='albums', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner.name} - {self.name}"

class Photo(models.Model):
    album = models.ForeignKey(GalleryAlbum, related_name='photos', on_delete=models.CASCADE)
    image_url = models.URLField()
    title = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title or self.image_url

class Post(models.Model):

    kulanici = models.ForeignKey('api.TrackedUser', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Comment(models.Model):

    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    author_avatar = models.URLField(blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author_name} - {self.post.title}"