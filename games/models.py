from django.db import models

class Category(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=150)
    premier = models.DateField()
    genre = models.CharField(max_length=100)
    character = models.TextField()
    preview_image = models.ImageField(upload_to='game_previfew_image/')
    description = models.TextField()
    size = models.CharField(max_length=50)
    file = models.FileField(upload_to='game_torrent/')
    triller_url = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name


class GameScreenshots(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='game_screenshots/')

    def __str__(self):
        return str(self.game)