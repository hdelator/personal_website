from django.db import models
from django.utils import timezone


class ContactMeForm(models.Model):

    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.subject}, {self.message}"  # rename object name for easy querying

    class Meta:
        verbose_name = 'Contact Form' # for admin interface (model naming)




