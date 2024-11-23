from django.contrib import admin

from .models import Comment, Forum

admin.site.register([Forum, Comment])
