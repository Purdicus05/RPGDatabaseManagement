# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Armour(models.Model):
    armour_id = models.AutoField(db_column='armour_ID', primary_key=True)  # Field name made lowercase.
    armour_name = models.CharField(max_length=64)
    armour_type = models.CharField(max_length=8)
    armour_armourclass = models.IntegerField(db_column='armour_armourClass')  # Field name made lowercase.
    armour_weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'armour'
        verbose_name_plural = 'Armour'
        verbose_name = 'Armour'

    def __str__(self):
        return f'{self.armour_name}'


class Characters(models.Model):
    character_id = models.AutoField(db_column='character_ID', primary_key=True)  # Field name made lowercase.
    character_name = models.CharField(max_length=24)
    character_class = models.ForeignKey('Classes', models.DO_NOTHING, db_column='character_class')
    character_race = models.ForeignKey('Races', models.DO_NOTHING, db_column='character_race')
    character_armourid = models.ForeignKey(Armour, models.DO_NOTHING, db_column='character_armourID')  # Field name made lowercase.
    character_weaponid = models.ForeignKey('Weapons', models.DO_NOTHING, db_column='character_weaponID', blank=True, null=True)  # Field name made lowercase.
    character_spellid = models.ForeignKey('Spells', models.DO_NOTHING, db_column='character_spellID', blank=True, null=True)  # Field name made lowercase.
    character_hitpoints = models.IntegerField(db_column='character_hitPoints')  # Field name made lowercase.
    character_level = models.IntegerField()
    character_strength = models.IntegerField()
    character_intelligence = models.IntegerField()
    character_dexterity = models.IntegerField()
    character_constitution = models.IntegerField()
    character_wisdom = models.IntegerField()
    character_playerid = models.ForeignKey('Players', models.DO_NOTHING, db_column='character_playerID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'characters'
        verbose_name_plural = 'Characters'
        verbose_name = 'Character'

    def __str__(self):
        return f'{self.character_name}'


class Classes(models.Model):
    class_name = models.CharField(primary_key=True, max_length=16)
    class_spellslots = models.IntegerField(db_column='class_spellSlots', blank=True, null=True)  # Field name made lowercase.
    class_strmod = models.IntegerField(db_column='class_strMod', blank=True, null=True)  # Field name made lowercase.
    class_charmod = models.IntegerField(db_column='class_charMod', blank=True, null=True)  # Field name made lowercase.
    class_wismod = models.IntegerField(db_column='class_wisMod', blank=True, null=True)  # Field name made lowercase.
    class_intmod = models.IntegerField(db_column='class_intMod', blank=True, null=True)  # Field name made lowercase.
    class_conmod = models.IntegerField(db_column='class_conMod', blank=True, null=True)  # Field name made lowercase.
    class_dexmod = models.IntegerField(db_column='class_dexMod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classes'
        verbose_name_plural = 'Classes'
        verbose_name = 'Class'

    def __str__(self):
        return f'{self.class_name}'


class Npc(models.Model):
    npc_id = models.AutoField(db_column='npc_ID', primary_key=True)  # Field name made lowercase.
    npc_type = models.CharField(max_length=32)
    npc_hp = models.IntegerField()
    npc_ac = models.IntegerField()
    npc_weaponid = models.ForeignKey('Weapons', models.DO_NOTHING, db_column='npc_weaponID', blank=True, null=True)  # Field name made lowercase.
    npc_spellid = models.ForeignKey('Spells', models.DO_NOTHING, db_column='npc_spellID', blank=True, null=True)  # Field name made lowercase.
    npc_race = models.ForeignKey('Races', models.DO_NOTHING, db_column='npc_race')

    class Meta:
        managed = False
        db_table = 'npc'
        verbose_name_plural = 'NPCs'
        verbose_name = 'NPC'

    def __str__(self):
        return f'{self.npc_type}'


class Players(models.Model):
    player_id = models.AutoField(db_column='player_ID', primary_key=True)  # Field name made lowercase.
    player_firstname = models.CharField(db_column='player_firstName', max_length=255)  # Field name made lowercase.
    player_surname = models.CharField(max_length=255)
    player_username = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'players'

    def __str__(self):
        return f'{self.player_username}'

class Races(models.Model):
    race_name = models.CharField(primary_key=True, max_length=32)
    race_darkvision = models.IntegerField(db_column='race_darkVision', blank=True, null=True)  # Field name made lowercase.
    race_strmod = models.IntegerField(db_column='race_strMod', blank=True, null=True)  # Field name made lowercase.
    race_charmod = models.IntegerField(db_column='race_charMod', blank=True, null=True)  # Field name made lowercase.
    race_wismod = models.IntegerField(db_column='race_wisMod', blank=True, null=True)  # Field name made lowercase.
    race_intmod = models.IntegerField(db_column='race_intMod', blank=True, null=True)  # Field name made lowercase.
    race_conmod = models.IntegerField(db_column='race_conMod', blank=True, null=True)  # Field name made lowercase.
    race_dexmod = models.IntegerField(db_column='race_dexMod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'races'
        verbose_name_plural = 'Races'
        verbose_name = 'Race'

    def __str__(self):
        return f'{self.race_name}'


class Spells(models.Model):
    spell_id = models.AutoField(db_column='spell_ID', primary_key=True)  # Field name made lowercase.
    spell_name = models.CharField(max_length=32)
    spell_school = models.CharField(max_length=16)
    spell_damage = models.IntegerField()
    spell_dmgtype = models.CharField(db_column='spell_dmgType', max_length=32)  # Field name made lowercase.
    spell_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spells'
        verbose_name_plural = 'Spells'
        verbose_name = 'Spell'

    def __str__(self):
        return f'{self.spell_name}'

class Weapons(models.Model):
    weapon_id = models.AutoField(db_column='weapon_ID', primary_key=True)  # Field name made lowercase.
    weapon_name = models.CharField(max_length=32)
    weapon_type = models.CharField(max_length=32)
    weapon_damagetype = models.CharField(db_column='weapon_damageType', max_length=32)  # Field name made lowercase.
    weapon_damageamount = models.IntegerField(db_column='weapon_damageAmount')  # Field name made lowercase.
    weapon_weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'weapons'
        verbose_name_plural = 'Weapons'
        verbose_name = 'Weapon'

    def __str__(self):
        return f'{self.weapon_name}'