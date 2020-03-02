from django.db import models

class Responce(models.Model): 
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    site_url = models.URLField()
    comment = models.TextField(max_length = 240)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    