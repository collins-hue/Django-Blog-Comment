from django.db import models

from tinymce.models import HTMLField


class Blog(models.Model):
    tittle = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=200, blank=False)
    content = HTMLField('Content')
    image = models.ImageField(upload_to='images/', null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.tittle

    class Meta:
        ordering = ["-date"]


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=False)
    comment = models.TextField(max_length=2000, null=False)
    date = models.DateField(auto_now=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date"]


class Socials(models.Model):
    Twitter = models.URLField(default='https://itsmurgor=09')
    reddit = models.URLField(default='https://itsmurgor=09')
    facebook = models.URLField(default='https://itsmurgor=09')
    instagram = models.URLField(default='https://itsmurgor=09')
