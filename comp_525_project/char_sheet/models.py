from django.db import models
from django.core import validators
from django.conf import settings

# Create your models here.

class Race(models.Model):
    """
    Model for races.

    Race information stored:
    char[255] name = ""
    char[12] mandatory_ability_increases //CSV of 6 ints. Defaults to all 0.
    int optional_ability_count = 0
    int speed = 30
    int size_category = 2

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
    name = models.CharField(default="", max_length=255)
    mandatory_ability_increases = models.CharField(
        max_length=12,
        validators=[validators.validate_comma_separated_integer_list],
        default="0,0,0,0,0,0")
    optional_ability_count = models.IntegerField(default=0)
    speed = models.IntegerField(default=30)
    size_category = models.IntegerField(default=2)
    darkvision = models.IntegerField(default=60)
    subrace_of = models.ForeignKey("self", on_delete=models.CASCADE,
                                   null=True, blank=True)

    def __str__(self):
        return self.name

class Spell(models.Model):
    """
    Model for spells

    Class information stored:

    Information listed in the SRD:
    name
    level (spell)
    school
    cast time (rounds, seconds, minutes)
    components (V,S,M,F) //5e might not have focus components
    duration (instantaneous, rounds, minutes, hours)
    range
    description (attacks, attack rolls, targets, saving throws, higher level
                 casting, targets (number, cube, cone))
    """
    name = models.CharField(default="", max_length=255)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class PlayerClass(models.Model):
    """
    Model for classes

    Class information stored:
    char[255] name = ""
    char[4] save proficiencies //CSV of indices. This will have a custom
                                 validator eventually. Defaults to all 0.
    int hit_die = 8 //d8 = 8
    int primary_ability = 0
    char[36] skill_proficiencies //CSV of either 1 or 0. This will have a
                                   custom validator eventually. Defaults to
                                   all 0.
    int skills_number = 2
    char[220] spell_slots //CSV. These values are grouped by tens; the first
                            ten represent spell slots at level 1, the second
                            ten represent spell slots at level 2, and so on.
                            This will be reformatted and given a custom
                            validator later. The first value for each level
                            (corresponding to level 0 spells) should be
                            interpreted as cantrips known, since no class has
                            0th level spell "slots"
    int spells_known = 0

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
    spellcasting information (cantrips? spontaneous? how many known? slots?)
    archetype information such as Primal Paths or Bardic Colleges
    Other features such as Wild Shape, Action Surge, or Unarmored Defense
    """
    name = models.CharField(default="", max_length=255)
    save_proficiencies = models.CharField(
        max_length=4,
        validators=[validators.validate_comma_separated_integer_list],
        default="0,1")
    hit_die = models.IntegerField(default=8)
    primary_ability = models.IntegerField(default=0)
    skill_proficiencies = models.CharField(
        max_length=36,
        validators=[validators.validate_comma_separated_integer_list],
        default="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
    skills_number = models.IntegerField(default=2)
    spell_slots = models.CharField(
        max_length=220,
        validators=[validators.validate_comma_separated_integer_list],
        default="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"
        "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"
        "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"
        "0,0,0,0,0,0,0,0,0,0,0,0")
    spells_known = models.IntegerField(default=0)
    spells = models.ManyToManyField(Spell)



    def __str__(self):
        return self.name

class Background(models.Model):
    """
    Model for backgrounds

    Background information stored:
    char[255] name = ""
    char[36] skill_proficiencies //CSV. this will have a custom validator

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
    name = models.CharField(default="", max_length=255)
    skill_proficiencies = models.CharField(
        max_length=36,
        validators=[validators.validate_comma_separated_integer_list],
        default="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

    def __str__(self):
        return self.name

class Character(models.Model):
    """
    Model for characters

    Character information listed:
    char[255] name = ""
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
    char[72] proficiencies //CSV of either 1 or 0. This will use a custom
                             validator eventually. Defaults to all 0.
    char[4096] notes = ""
    settings.AUTH_USER_MODEL owner
    settings.AUTH_USER_MODEL[] can_view
    settings.AUTH_USER_MODEL[] can_edit

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
    name = models.CharField(default="", max_length=255)
    player_class = models.ForeignKey(PlayerClass, default=1, on_delete=models.SET_DEFAULT)
    background = models.ForeignKey(Background, default=1, on_delete=models.SET_DEFAULT)
    race = models.ForeignKey(Race, default=1, on_delete=models.SET_DEFAULT)
    alignment = models.CharField(default="NN", max_length=2)
    experience = models.IntegerField(default=0)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    max_hp = models.IntegerField(default=0)
    proficiencies = models.CharField(
        max_length=72,
        validators=[validators.validate_comma_separated_integer_list],
        default="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"
                "0,0,0,0,0,0")
    notes = models.CharField(default="", max_length=4096)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='+')
    can_view = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='+')
    can_edit = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='+')
    equipment = models.ManyToManyField("Item")
    equipment_quantities = models.CharField(
        max_length=4096,
        validators=[validators.validate_comma_separated_integer_list],
        null=True,
        blank=True)
    current_hp = models.IntegerField(default=0)
    temp_hp = models.IntegerField(default=0)


    def __str__(self):
        return "Character: " + self.name

class Attack(models.Model):
    """
    Model for attacks

    Item information listed:
    char[255] damage_roll = "1d6"
    char damage_type = "b"
    char[255] versatile_damage (can be null)
    int short_range = 0
    int long_range = 0
    char[255] properties = "" //CSV. This will have a validator eventually

    Information listed in the PHB (equipment):
    name
    cost
    damage
    damage type
    weight
    properties (light, finesse, thrown, two-handed, versatile, ammunition...)
    """
    name = models.CharField(default="", max_length=255)
    damage_roll = models.CharField(default="1d6", max_length=255)
    damage_type = models.CharField(default="b", max_length=1)
    versatile_damage = models.CharField(null=True, blank=True, max_length=255)
    short_range = models.IntegerField(default=0)
    long_range = models.IntegerField(default=0)
    properties = models.CharField(default="", max_length=255)

    def __str__(self):
        return self.name

class Armor(models.Model):
    """
    Model for armor

    Item information listed:
    int base_armor_class = 14
    int min_dex = 9001
    int min_str = 0
    bool stealth_disadvantage = False

    Information listed in the PHB:
    name
    cost
    AC
    min STR
    stealth disadvantage?
    weight
    """
    name = models.CharField(default="", max_length=255)
    # interpret a value of 0 here as being a straight up bonus
    base_armor_class = models.IntegerField(default=14)
    max_dex = models.IntegerField(default=9001) # watch someone break this
    min_str = models.IntegerField(default=0)
    stealth_disadvantage = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Item(models.Model):
    """
    Model for gear

    Item information listed:
    char[255] name = ""
    float cost = 0
    float weight = 0
    Attack attack (can be null)
    Armor armor (can be null)
    bool requires_proficiency = False
    int generic_proficiency (can be null)
        Generic proficiencies are (starting from the 0th one):
        light armor
        medium armor
        heavy armor
        simple weapons
        martial weapons

    Information listed in the PHB:
    name
    cost
    weight
    description
    """
    name = models.CharField(default="", max_length=255)
    cost = models.DecimalField(default=0, max_digits=10, decimal_places=5)
    weight = models.DecimalField(default=0, max_digits=10, decimal_places=5)
    attack = models.ForeignKey(Attack, null=True, blank=True)
    armor = models.ForeignKey(Armor, null=True, blank=True)
    requires_proficiency = models.BooleanField(default=False)
    generic_proficiency = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Campaign(models.Model):
    """
    Class for campaigns

    Has two fields:
    char[255] name = ""
    settings.AUTH_USER_MODEL[] players
    settings.AUTH_USER_MODEL[] game_masters
    """

    name = models.CharField(default="", max_length=255)
    players = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                     related_name='+')
    game_masters = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                          related_name='+')
