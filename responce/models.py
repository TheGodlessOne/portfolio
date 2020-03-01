from django.db import models

class Responce(models.Model): 
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    site_url = models.URLField()
    comment = models.TextField(max_length = 240)
