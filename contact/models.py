from django.db import models
from datetime import datetime

class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name    = models.CharField(max_length=30)
    email   = models.CharField(max_length=80)
    phone   = models.CharField(max_length=15)
    message = models.TextField(blank=True) #optional
    date    = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

    