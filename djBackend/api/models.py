from django.db import models

# Create your models here.
class Player(models.Model):
    userName = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    userID = models.CharField(max_length=100)
    joinDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email