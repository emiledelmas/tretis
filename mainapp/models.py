from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=155,default="/media/profile_pics/red.png")
    level = models.IntegerField(default=1)
    score = models.IntegerField(default=20)
    def __str__(self):
        return f'{self.user.username} Profile'

class Profiles_Picture(models.Model):
    title = models.CharField(max_length=155,default="Image_Profile")
    image = models.ImageField(upload_to="profile_pics")
    required_level = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

class Historique(models.Model):
    username = models.CharField(max_length=50,default='user')
    rank = models.IntegerField()
    level = models.IntegerField()
    score = models.IntegerField()
    game_score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.username} Game'
        