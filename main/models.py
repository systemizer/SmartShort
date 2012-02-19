from django.db import models


class URL(models.Model):
    url = models.URLField(verify_exists=True)
    shared_url = models.URLField(null=True,blank=True) #auto generated and shared to people
    shared = models.TextField()
    scrolled = models.IntegerField(null=True,blank=True)

