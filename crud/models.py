from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    role_choices = [
        ("Batsman", "Batsman"),
        ("Bowler", "Bowler"),
        ("All_Rounder", "All_Rounder"),
        ("Wicket_Keeper", "Wicket_Keeper"),
    ]
    country_choices = [
        ("India", "India"),
        ("Bangladesh","Bangladesh"),
        ("Sri_Lanka","Sri_Lanka"),
        ("Australia","Australia"),
        ("NewZeland","NewZeland"),
        ("England","England"),
        ("South_Africa","South_Africa"),
        ("West_Indies", "West_Indies"),
        ("Other","Other"),
    ]

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    role = models.CharField(max_length=100, choices=role_choices)
    country = models.CharField(max_length=100, choices=country_choices)
    profile_pic = models.ImageField(upload_to="player/")
    is_captain = models.BooleanField(default=False)
    fav_food = models.ManyToManyField(Food)

    def __str__(self):
        return f"{self.name} - {self.role}"