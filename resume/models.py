from django.db import models
from django.utils import timezone

class ContactMeModel(models.Model):

    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=500)
    # text = models.TextField()
    message = models.TextField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.name}, {self.email}, {self.subject}, {self.message}"  # rename object name for easy querying

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = 'Contact Form'  # for admin interface (model naming)

