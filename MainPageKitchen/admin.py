from django.contrib import admin

# Register your models here
from .models import BlogCategory, BlogPost

admin.site.register(BlogCategory)
admin.site.register(BlogPost)