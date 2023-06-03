from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    pic=models.ImageField(upload_to='catalog/')
    description = models.TextField()

    def __str__(self):
        return self.name
PRODUCT_TAG=(
    ('new','new'),
    ('top','top'),
    ('best','best'),
    ('featured','featured'),
    ('popular','popular'),
    ('trending','trending'),
    ('awesome','awesome'),
    ('beautiful','beautiful'),
     ('stlish','stylish'),
    
)
AVAILABILITY=(
    ('In Stock','In Stock'),
    ('Out of Stock','Out of Stock'),
    ('Preorder','Preorder'),
)

class products(models.Model):
    name=models.CharField(max_length=200)
    catid=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="categoryname")
    pic1=models.ImageField(upload_to='catalog/')
    pic2=models.ImageField(upload_to='catalog/',blank=True,null = True)
    pic3=models.ImageField(upload_to='catalog/',blank=True,null = True)
    pic4=models.ImageField(upload_to='catalog/',blank=True,null = True)
    mrp=models.IntegerField()
    sellingprice=models.IntegerField()
    description=HTMLField(blank=True,null = True)
    specification=models.CharField(max_length=600,default='')
    tag=models.CharField(max_length=200,choices=PRODUCT_TAG)
    available=models.CharField(max_length=200,choices=AVAILABILITY)
    class Meta:
        db_table='products'
    def __str__(self):
        return self.name