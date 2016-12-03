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
                "name": obj.name
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
                "name": obj.name
            }
        return super(RaceEncoder, self).default(obj)

