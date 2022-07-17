from django.db import models


class Post(models.Model):
    body = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField('images.Image')

    def __str__(self):
        return str(self.body)
