from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100)
    founder_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Gamer(models.Model):
    full_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, unique=True)
    rating = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='static/assets/avatars/')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def  __str__(self):
        return self.nickname



