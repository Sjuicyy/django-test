from xml.etree.ElementTree import Comment
from django.db import models

# Create your models here.
class product(models.Model):
    name = models.TextField()
    price =models.TextField()
    summary=models.TextField(default="null")
    Comment=models.TextField(default="null")
