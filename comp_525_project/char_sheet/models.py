from django.db import models

# Create your models here.

class Race(models.Model):
    """
    Model for races.

    Race information stored:
    char[255] name

    Information listed in the PHB:
    name
    description
    typical character names
    ability score increases
    age information
    typical alignment
    size category
    height and weight
    base speed
    languages
    Darkvision
    rolls with advantage
    proficiencies
    other traits such as Trance, Stonecunning Sunlight Sensitivity, and Lucky
    subraces
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PlayerClass(models.Model):
    """
    Model for classes

    Class information stored:
    char[255] name

    Information listed in the PHB:
    name
    description
    hit die
    primary ability
    save proficiencies
    armor and weapon proficiencies
    skill proficiencies (pick x of ...)
    tool proficiencies
    starting equipment
    class specific traits such as Rage or Bardic Inspiration
    spellcasting information (cantrips? spontaneous? how many knows? slots?)
    archetype information such as Primal Paths or Bardic Colleges
    Other features such as Wild Shape, Action Surge, or Unarmored Defense
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Background(models.Model):
    """
    Model for backgrounds

    Background information stored:
    char[255] name

    Information listed in the PHB:
    name
    description
    proficiencies
    languages
    starting equipment
    personality traits
    ideals
    bonds
    flaws
    other features such as Shelter of the Faithful, False Identity, or Wanderer
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Character(models.Model):
    """
    Model for characters

    Character information listed:
    char[255] name
    PlayerClass player_class = (id 1)
    Background background = (id 1)
    Race race = (id 1)
    char[2] alignment
    int experience = 0
    int strength = 10
    int dexterity = 10 = 10
    int constitution = 10
    int intelligence = 10
    int wisdom = 10
    int charisma = 10
    int max_hp = 0
    int proficiencies_mask //this will be replaced with a CharField containing
                             CSV of bools soon
    char[4096] notes

    Information listed in the character sheet at the end of the PHB:
    name
    class and level
    background
    player name
    race
    alignment
    experience
    STR (and modifier)
    DEX  (and modifier)
    CON (and modifier)
    INT (and modifier)
    WIS (and modifier)
    CHA (and modifier)
    inspiration
    proficiency bonus
    save proficiencies
    skill proficiencies
    passive perception
    languages
    other proficiencies
    AC
    initiative bonus
    speed
    max HP
    current HP
    temporary HP
    total hit dice
    current hit dice
    death save counter
    "attacks & spellcasting" (name, attack bonus, damage)
    equipment
    cash money
    personality traits
    ideals
    bonds
    flaws
    other features and traits
    age
    height
    weight
    eyes
    skin
    hair
    appearance
    backstory
    "allies and organizations"
    other features and traits
    "treasure"
    spellcasting ability
    spell save DC
    spell attack bonus
    cantrips
    for each spell level:
        total number of slots
        slots expended
        spells of that level
            if prepared
    """
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


