from django.db import models


class Post(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return str(self.image)
