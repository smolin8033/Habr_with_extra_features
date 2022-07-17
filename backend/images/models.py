from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    content = models.ImageField(upload_to='posts')

    def __str__(self):
        return str(self.title)
