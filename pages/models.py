from django.db import models

# Create your models here.
from django.urls import reverse


class Note(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    text = models.TextField(null=True)
    image = models.ImageField(upload_to='note/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug":self.slug})