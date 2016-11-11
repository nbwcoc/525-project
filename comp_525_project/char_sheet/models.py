from django.db import models

# Create your models here.

class Race(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PlayerClass(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Background(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=255)
    player_class = models.ForeignKey(PlayerClass, default=1, on_delete=models.SET_DEFAULT)
    background = models.ForeignKey(Background, default=1, on_delete=models.SET_DEFAULT)
    race = models.ForeignKey(Race, default=1, on_delete=models.SET_DEFAULT)
    alignment = models.CharField(max_length=2)
    experience = models.IntegerField(default=0)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    max_hp = models.IntegerField(default=0)
    proficiencies_mask = models.IntegerField()
    notes = models.CharField(max_length=4096)

    def __str__(self):
        return "Character: " + self.name

# CREATE TABLE IF NOT EXISTS character (
#     id integer PRIMARY KEY,
#     name text,
#     class integer,
#     background integer,
#     race integer,
#     alignment text,
#     experience integer,
#     strength integer,
#     dexterity integer,
#     constitution integer,
#     intelligence integer,
#     wisdom integer,
#     charisma integer,
#     max_hp integer,
#     proficiencies_mask integer,
#     notes text
# );


