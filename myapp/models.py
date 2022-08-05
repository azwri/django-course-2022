from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Flower(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=False)
        super().save()
    
    def get_absolute_url(self):
        return reverse('myapp:detail', kwargs={'slug': self.slug})