from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.CharField(max_length=30,primary_key=True)
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Country = models.CharField(max_length=30)

class Book(models.Model):
    ISBN = models.CharField(max_length=13,primary_key=True,unique=True)
    Title = models.CharField(max_length=100)
    AuthorID = models.CharField(max_length=30)
    Publisher = models.CharField(max_length=100)
    PublishDate = models.CharField(max_length=30)
    Price = models.IntegerField()



    
