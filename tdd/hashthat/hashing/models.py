from django.db import models
from django.forms.fields import CharField

# Create your models here.

class Hash(models.Model):
    text = models.TextField()
    hash = models.CharField(max_length=64)

    class Meta:
        unique_together = ("text", "hash")
