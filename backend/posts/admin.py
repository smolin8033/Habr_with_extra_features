from django.contrib import admin

from posts.models import Post, PostImage


@admin.register(Post)
class Post(admin.ModelAdmin):
    pass


@admin.register(PostImage)
class PostImage(admin.ModelAdmin):
    pass
