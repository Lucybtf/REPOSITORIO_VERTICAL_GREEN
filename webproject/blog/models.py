from django.db import models

# Create your models here.
 
class Post(models.Model):
	title = models.CharField(max_length=100) #char de 100
	url = models.CharField(max_length=150) #char de 150
	content = models.TextField() # text