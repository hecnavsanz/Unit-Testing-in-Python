from django.db import models

# Create security models.
class User(models.Model):

    username = models.CharField(name='username', primary_key=True, max_length=20)
    password = models.CharField(name='password', blank=False, null=False, max_length=20)

    def __str__(self):
        return self.username
