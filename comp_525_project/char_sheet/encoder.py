"""
Define JSON encoders for use with our models.
"""
from django.core.serializers.json import DjangoJSONEncoder
from . import models

class CharacterEncoder(DjangoJSONEncoder):
    """
    Usage: JsonResponse(<single Character object>,
                        encoder=encoder.CharacterEncoder, safe=False)
    Formats an object for use with the default JSON encoder. For more
    information, see DjangoJSONEncoder.
    """
    def default(self, obj):
        if isinstance(obj, models.Character):
            return {
                "name" = obj.name
                "player_class" = obj.player_class
                "background" = obj.background
                "race" = obj.race
                "alignment" = obj.alignment
                "experience" = obj.experience
                "strength" = obj.strength
                "dexterity" = obj.dexterity
                "constitution" = obj.constitution
                "intelligence" = obj.intelligence
                "wisdom" = obj.wisdom
                "charisma" = obj.charisma
                "max_hp" = obj.max_hp
                "proficiencies" = obj.proficiencies
                "notes" = obj.notes
                "owner" = obj.owner
                "can_view" = obj.can_view
                "can_edit" = obj.can_edit
                "equipment" = obj.equipment
                "equipment_quantities" = obj.equipment_quantities
                "current_hp" = obj.current_hp
                "temp_hp" = obj.temp_hp
            }
        return super(CharacterEncoder, self).default(obj)

class BackgroundEncoder(DjangoJSONEncoder):
    """
    Usage: JsonResponse(<single Background object>,
                        encoder=encoder.BackgroundEncoder, safe=False)
    Formats an object for use with the default JSON encoder. For more
    information, see DjangoJSONEncoder.
    """
    def default(self, obj):
        if isinstance(obj, models.Background):
            return {
                "name" = obj.name
                "skill_proficiencies" = obj.skill_proficiencies
            }
        return super(BackgroundEncoder, self).default(obj)

class PlayerClassEncoder(DjangoJSONEncoder):
    """
    Usage: JsonResponse(<single PlayerClass object>,
                        encoder=encoder.PlayerClassEncoder, safe=False)
    Formats an object for use with the default JSON encoder. For more
    information, see DjangoJSONEncoder.
    """
    def default(self, obj):
        if isinstance(obj, models.PlayerClass):
            return {
                "name": obj.name
                "save_proficiencies" = obj.save_proficiencies
                "hit_die" = obj.hit_die
                "primary_ability" = obj.primary_ability
                "skill_proficiencies" = obj.skill_proficiencies
                "skills_number" = obj.skills_number
                "spell_slots" = obj.spell_slots
                "spells_known" = obj.spells_known
        }
        return super(PlayerClassEncoder, self).default(obj)

class RaceEncoder(DjangoJSONEncoder):
    """
    Usage: JsonResponse(<single Race object>, encoder=encoder.RaceEncoder,
                        safe=False)
    Formats an object for use with the default JSON encoder. For more
    information, see DjangoJSONEncoder.
    """
    def default(self, obj):
        if isinstance(obj, models.Race):
            return {
                "name" = obj.name
                "mandatory_ability_increases" = obj.mandatory_ability_increases
                "optional_ability_count" =  obj.optional_ability_count
                "speed" = obj.speed
                "size_category" = obj.size_category
                "darkvision" = obj.darkvision
                "subrace_of" = obj.subrace_of
            }
        return super(RaceEncoder, self).default(obj)

def AttackEncoder(DjangoJSONEncoder):
    """
    Usage: JsonResponse(<single Attack object>, encoder=encoder.AttackEncoder,
                        safe=False)
    Formats an object for use with the default JSON encoder. For more 
    information, see DjangoJSONEncoder.
    """
    def default(self, obj):
        if isinstance(obj, models.Attack):
            return {
                "name" = obj.name
                "damage_roll" = obj.damage_roll
                "damage_type" = obj.damage_type
                "versatile_damage" = obj.versatile_damage
                "short_range" = obj.short_range
                "long_range" = obj.long_range
                "properties" = obj.properties
            }
        return super(AttackEncoder, self).default(obj)

def ArmorEncoder(DjangoJSONEncoder):
    """
    Usage: JsonResponse(<single Armor object>, encoder=encoder.ArmorEncoder,
                        safe=False)
    Formats an object for use with the default JSON encoder. For more 
    information, see DjangoJSONEncoder.
    """
    def default(self, obj):
        if isinstance(obj, models.Armor):
            return {
                "name" = obj.name
                "base_armor_class" = obj.base_armor_class
                "max_dex" = obj.max_dex
                "min_str" = obj.min_str
                "stealth_disadvantage" = obj.stealth_disadvantage
            }
        return super(ArmorEncoder, self).default(obj)

def ItemEncoder(DjangoJSONEncoder):
    """
    Usage: JsonResponse(<single Item object>, encoder=encoder.ItemEncoder,
                        safe=False)
    Formats an object for use with the default JSON encoder. For more 
    information, see DjangoJSONEncoder.
    """
    def default(self, obj):
        if isinstance(obj, models.Item):
            return {
                "name" = obj.name
                "cost" = obj.cost
                "weight" = obj.weight
                "attack" = obj.attack
                "armor" = obj.armor
                "requires_proficiency" = obj.requires_proficiency
                "generic_proficiency" = obj.generic_proficiency
            }
        return super(ItemEncoder, self).default(obj)
