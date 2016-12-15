from django.db import models


class ContactForm(models.Model):
    subject = models.CharField(max_length=100)
    sender = models.EmailField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

