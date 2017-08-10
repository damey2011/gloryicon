from django.contrib import admin

# Register your models here.
from blog.models import BlogPost, Comment, BlogCategory, ContactFormModel

admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(BlogCategory)
admin.site.register(ContactFormModel)
