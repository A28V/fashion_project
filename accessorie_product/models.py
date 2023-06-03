from django.db import models

# Create your models here.


class AccessorieProductConfig(models.Model):
    name=models.CharField(max_length=200)
    catid=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="categoryname")