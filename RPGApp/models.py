from django.db import models

# Create your models here.

class players (models.Model):
    player_ID = models.IntegerField(primary_key=True)
    player_firstName = models.CharField(max_length=255)
    player_surname = models.CharField(max_length=255)
    player_username = models.CharField(max_length=255)

class spells (models.Model):
    spell_ID = models.IntegerField(primary_key=True)
    spell_name = models.CharField(max_length=32)
    spell_school = models.CharField(max_length=16)
    spell_damage = models.IntegerField()
    spell_dmgType = models.CharField(max_length=32)
    spell_level = models.IntegerField()

class races (models.Model):
    race_name = models.CharField(max_length=32,primary_key=True)
    race_darkVision = models.BooleanField()
    race_strMod = models.IntegerField()
    race_charMod = models.IntegerField()
    race_wisMod = models.IntegerField()
    race_intMod = models.IntegerField()
    race_conMod = models.IntegerField()
    race_dexMod = models.IntegerField()

class classes (models.Model):
    class_name = models.CharField(max_length=32,primary_key=True)
    class_spellSlots= models.IntegerField()
    class_strMod = models.IntegerField()
    class_charMod = models.IntegerField()
    class_wisMod = models.IntegerField()
    class_intMod = models.IntegerField()
    class_conMod = models.IntegerField()
    class_dexMod = models.IntegerField()

class armour (models.Model):
    armour_ID = models.IntegerField(primary_key=True)
    armour_name = models.CharField(max_length=64)
    armour_type = models.CharField(max_length=8)
    armour_armourClass = models.IntegerField()
    armour_weight = models.IntegerField()

class weapons (models.Model):
    weapon_ID = models.IntegerField(primary_key=True)
    weapon_name = models.CharField(max_length=32)
    weapon_type = models.CharField(max_length=32)
    weapon_damageType = models.CharField(max_length=32)
    weapon_damageAmount = models.IntegerField()
    weapon_weight = models.IntegerField()

class characters(models.Model):
    character_ID = models.IntegerField(primary_key=True)
    character_name = models.CharField(max_length=24)
    character_class = models.ForeignKey(classes, on_delete=models.SET_NULL, null=False, blank=True)
    character_race = models.ForeignKey(races, on_delete=models.SET_NULL, null=False, blank=True)
    character_armourID = models.ForeignKey(armour, on_delete=models.SET_NULL, null=True, blank=True)
    character_weaponID = models.ForeignKey(weapons, on_delete=models.SET_NULL, null=True, blank=True)
    character_spellID = models.ForeignKey(spells, on_delete=models.SET_NULL, null=True, blank=True)
    character_hitPoints = models.IntegerField()
    character_level = models.IntegerField()
    character_strength = models.IntegerField()
    character_intelligence = models.IntegerField()
    character_dexterity = models.IntegerField()
    character_constitution = models.IntegerField()
    character_wisdom = models.IntegerField()
    character_playerID = models.ForeignKey(players, on_delete=models.SET_NULL, null=False, blank=True)

class npc (models.Model):
    npc_ID = models.IntegerField(primary_key=True)
    npc_type = models.CharField(max_length=32)
    npc_hp = models.IntegerField()
    npc_ac = models.IntegerField()
    npc_weaponID = models.IntegerField()
    npc_spellID = models.IntegerField()
    npc_race = models.CharField(max_length=32)