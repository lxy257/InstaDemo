from django.contrib import admin

# Register your models here.
from Insta.models import Post, Like, InstaUser, UserConnection

admin.site.register(Post)

admin.site.register(InstaUser)

admin.site.register(Like)

admin.site.register(UserConnection)