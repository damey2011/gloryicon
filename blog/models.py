from django.contrib.auth.models import User
from django.contrib.sitemaps import Sitemap
from django.db import models


# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse


class BlogCategory(models.Model):
    category = models.CharField(max_length=200)
    details = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class Comment(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.email


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User)
    likes = models.IntegerField(default=0)
    post_image = models.ImageField(upload_to="media", blank=True)
    category = models.ForeignKey(BlogCategory, null=True)
    slug = models.CharField(blank=True, max_length=150)
    seo_keywords = models.TextField(blank=True)
    seo_desc = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog-post', kwargs={'slug': self.slug})

    def get_no_comments(self):
        return Comment.objects.filter(parent=self.id).count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.timestamp


class StaticPagesSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'home',
            'all_posts'
        ]

    def location(self, item):
        return reverse(item)


class StandAloneImageUpload(models.Model):
    image = models.ImageField(upload_to='image-uploads')


class ContactFormModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
