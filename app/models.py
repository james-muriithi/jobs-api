from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Job(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True, unique=True)
    location = models.CharField(max_length=150, null=True)
    company = models.CharField(max_length=150, null=True)
    job_type = models.CharField(max_length=150, null=True)
    salary = models.CharField(max_length=150, null=True)
    link = models.CharField(max_length=150, null=True)
    post_date = models.CharField(max_length=150, null=True)
    summary = models.TextField(null=True)
    job_type = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save_post(self):
        self.slug = slugify(self.title)
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
