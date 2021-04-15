from django.db import models

# Create your models here.
from django.urls import reverse

NDS = 22

class Note(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=100)
    text = models.TextField(null=True)
    image = models.ImageField(upload_to='note/')
    price = models.DecimalField(default=0.00,max_digits=6, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(default=0, null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug":self.slug})

    def full_name(self):
        #Вычисляемое поле full_name
        return " ".join([self.family, self.name]).capitalize()

    def text_upper(self):
        return self.text.upper()

    def computing_price(self):
        # Вычисляемое поле
        return self.price * self.quantity

    def nalog_nds(self):
        return (self.computing_price() * NDS) / 100
