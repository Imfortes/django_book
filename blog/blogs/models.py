from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    verbose_name = 'Пост'
    verbose_name_plural = 'Посты'

    title = models.CharField(max_length=250, verbose_name='Пост')
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title