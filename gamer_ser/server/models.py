from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4 as uidg

class UserProfile(models.Model):
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE, related_name='profile')
    userID = models.CharField(max_length=255, default=uidg(), unique=True)
    current_state = models.CharField(max_length=255, default='ideal')
    img = models.CharField(max_length=255, default='https://cdn-icons-png.flaticon.com/512/5281/5281619.png')
    XP = models.BigIntegerField(default=0)
    lvl = models.IntegerField(default=0)
    friends = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='friend_profiles')

    def __str__(self):
        return str(self.user)