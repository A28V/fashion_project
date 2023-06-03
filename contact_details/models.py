from django.db import models

# Create your models here.
class ContactDetails(models.Model):
	name=models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	subject = models.CharField(max_length=50)
	contact_number = models.CharField(max_length=50)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)  