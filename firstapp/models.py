from django.db import models
from django.urls import reverse
# Create your models here.
class profileinfo(models.Model):
    name=models.CharField(max_length=200,default='')
    Description=models.CharField(max_length=200)
    Author=models.CharField(max_length=200)
    published_date=models.CharField(max_length=200)
    image=models.ImageField(upload_to='profile_image',blank=True)
    pdf=models.FileField(upload_to='pdf',blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main")
