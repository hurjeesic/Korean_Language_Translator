from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Patter(models.Model):
    patter_str = models.CharField(max_length=200, primary_key=True)
    meaning_str = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patter_str
