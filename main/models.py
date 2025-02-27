from django.db import models

class Register(models.Model):
    name = models.CharField('Name', max_length=15)
    password = models.CharField('Password', max_length=20)
    password1 = models.CharField('Confirm your password', max_length=20)

    def __str__(self):
        return self.name

