from django.db import models
from django.utils.text import slugify
class UsersConfig(models.Model):
	email = models.CharField(max_length=50)
	password=models.CharField(max_length=50)
    # def save(self, *args, **kwargs):
    #   self.slug = slugify(self.title)
    #   super(UsersConfig, self).save(*args, **kwargs)
# Create your models here.
