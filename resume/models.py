from django.db import models
from django.utils import timezone

class Search(models.Model):
    search_text = models.CharField(max_length=80)
    search_date = models.DateTimeField('search date')
