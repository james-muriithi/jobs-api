from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Job(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    company = models.CharField(max_length=150, null=True, blank=True)
    job_type = models.CharField(max_length=150, null=True, blank=True)
    salary = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=150, unique=True)
    post_date = models.CharField(max_length=150, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    full_text = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
