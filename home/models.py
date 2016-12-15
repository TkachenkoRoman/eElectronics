from django.db import models


# Create your models here.
class SignUpForm(models.Model):
    email = models.EmailField('Enter email here')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email


