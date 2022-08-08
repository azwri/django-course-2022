from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from datetime import datetime


class Flower(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, default='', unique=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + \
            f'-{self.user.id}-' + \
            datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        super().save()
    
    def get_absolute_url(self):
        return reverse('myapp:detail', kwargs={'slug': self.slug})

class Category(models.Model):
    name = models.CharField( max_length=255)
    slug = models.SlugField(blank=True, default='', unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + \
            datetime.now().strftime("-%Y-%m-%d-%H-%M%-%S-") + \
            f'{self.user.id}')
        
        super().save()
        

    def get_absolute_url(self):
        return reverse('myapp:category_detail', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, default='', unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + \
            datetime.now().strftime("-%Y-%m-%d-%H-%M%-%S-") + \
            f'{self.user.id}')
        super().save()

    def get_absolute_url(self):
        return reverse('myapp:tag', kwargs={'slug': self.slug})