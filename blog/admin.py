from django.contrib import admin
from .models import Post



admin.site.register(Post)
# why did we use .models instead of blog.models
