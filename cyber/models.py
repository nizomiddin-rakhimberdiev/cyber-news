from django.contrib.auth.models import AbstractUser
from django.db import models


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


class Gamer(AbstractUser):
    rating = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='static/assets/avatars/')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username


class Group(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image_logo = models.ImageField(upload_to='static/assets/images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Gamer_Group(models.Model):
    name = models.CharField(max_length=100)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    gamer_id = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Game_Club(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    game_club_image = models.ImageField(upload_to='static/assets/images/')

    def __str__(self):
        return self.name


class Battle(models.Model):
    title = models.CharField(max_length=100)
    battle_data = models.DateTimeField()
    game_club_id = models.ForeignKey(Game_Club, on_delete=models.CASCADE)
    battle_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Battle_Group(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    battle_id = models.ForeignKey(Battle, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group_id.name} {self.battle_id.title}"


class Battle_News(models.Model):
    battle_id = models.ForeignKey(Battle, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Battle_News_Images(models.Model):
    news_image = models.ImageField(upload_to='static/assets/images/', blank=True, null=True)
    battle_id = models.ForeignKey(Battle, on_delete=models.CASCADE)
    battle_news_id = models.ForeignKey(Battle_News, on_delete=models.CASCADE)

    def __str__(self):
        return self.battle_news_id.title


class Updates_news(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    updates_news_video = models.FileField(upload_to='static/assets/videos/')
    updates_news_image = models.ImageField(upload_to='static/assets/images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class GameCommentary(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    commentary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.game_id} {self.commentary}"
