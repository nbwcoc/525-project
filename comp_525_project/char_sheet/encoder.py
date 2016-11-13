from django.core.serializers.json import DjangoJSONEncoder
from . import models

class CharacterEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.Character):
            return {
                "name": obj.name,
                "player_class": obj.player_class.id,
                "background": obj.background.id,
                "race": obj.race.id,
                "alignment": obj.alignment,
                "experience": obj.experience,
                "strength": obj.strength,
                "dexterity": obj.dexterity,
                "constitution": obj.constitution,
                "intelligence": obj.intelligence,
                "wisdom": obj.wisdom,
                "charisma": obj.charisma,
                "max_hp": obj.max_hp,
                "proficiencies_mask": obj.proficiencies_mask,
                "notes": obj.notes
            }
        return super(CharacterEncoder, self).default(obj)

class BackgroundEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.Background):
            return {
                "name": obj.name
            }
        return super(BackgroundEncoder, self).default(obj)

class PlayerClassEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.PlayerClass):
            return {
                "name": obj.name
            }
        return super(PlayerClassEncoder, self).default(obj)

class RaceEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.Race):
            return {
                "name": obj.name
            }
        return super(RaceEncoder, self).default(obj)

