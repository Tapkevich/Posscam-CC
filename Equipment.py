import csv
import BaseStats
from math import floor


class EquipmentBase(object):
    def __init__(self, key, name="None"):
        self.name = name
        self.key = key
        self.type = str
        self.slot = str
        self.stat_bonuses = {
            "Strength": 0,
            "Dexterity": 0,
            "Endurance": 0,
            "Technic": 0,
            "Speed": 0,
            "HitChance": 0,
            "Crit": 0,
            "DodgeChance": 0,
            "DebuffEfficiency": 0,
            "ResPhys": 0,
            "ResChem": 0,
            "ResThermo": 0,
            "Heal": 0,
            "Power": 0
        }





class EquipmentCommon(EquipmentBase):
    def __init__(self, key, rarity, name="None"):
        EquipmentBase.__init__(self, key, name)
        self.rarity = EquipmentRarity(rarity)
        self.get_common_equip_stats()

    def get_common_equip_stats(self):
        stat_source = csv.DictReader(open(BaseStats.ITEM_COMMON_BASES_CSV))
        for row in stat_source:
            if row["Key"] == self.key:
                # Ключ предмета, должен совпадать с одним из ключей в таблице EquipmentCommon
                # Мы смотрим, что по табличным значениям предмет действительно дает бонус к статам сам по себе
                # И если да, то увеличиваем этот бонус учитывая рарность
                if row["BonusType1"] != "None" and int(row["BonusAmount1"]) != 0:
                    self.stat_bonuses[row["BonusType1"]] += floor(int(row["BonusAmount1"]) * self.rarity.multi_stats)
                if row["BonusType2"] != "None" and int(row["BonusAmount2"]) != 0:
                    self.stat_bonuses[row["BonusType2"]] += floor(int(row["BonusAmount2"]) * self.rarity.multi_stats)
                # Так как power задается в отдельном столбце и со своим модификатором, его мы добавляем отдельно.
                if int(row["Power"]) != 0:
                    self.stat_bonuses["Power"] = int(row["Power"]) * self.rarity.multi_power
                self.type = row["Type"]
                self.slot = row["Slot"]


class EquipmentRarity(object):
    def __init__(self, key):
        self.key = key
        source = csv.DictReader(open(BaseStats.ITEM_RARITY_COEF_CSV))
        for row in source:
            if len(row["Rarity"]) == 0:
                continue
            elif self.key == row["Rarity"]:
                self.multi_power = float(row["MultiPower"])
                self.multi_stats = float(row["MultiStats"])
                self.multi_salvage = float(row["MultiSalvage"])


class EquipmentUnique(EquipmentBase):

    def __init__(self, key, name="None"):
        self.key = key
        EquipmentBase.__init__(self, key, name)
        meta_source = csv.DictReader(open(BaseStats.ITEM_UNIQUE_KEYS))
        for row in meta_source:
            if row["Key"] == self.key and row["Rarity"] in BaseStats.RARITY_LIST:
                self.rarity = row["Rarity"]
            else:
               raise Exception("Unique item {} dosen't have apropriate rarity ".format(self.key))
        self.get_unique_equip_stats()

    def get_unique_equip_stats(self):
        stat_source = csv.DictReader(open(BaseStats.ITEM_UNIQUE_STATS_CSV))
        for row in stat_source:
            if row["Key"] == self.key:
                self.stat_bonuses[row["BonusType"]] += int(row["BonusAmount"])

        meta_source = csv.DictReader(open(BaseStats.ITEM_UNIQUE_KEYS))
        for row in meta_source:
            if row["Key"] == self.key:
                self.type = row["Type"]
                self.slot = row["Slot"]

class EquipmentUtility:
    @staticmethod
    def check_weapon_type(merc, weapon):
        check = False
        if weapon.type == merc.mercenary_class.merc_weapon_type:
            check = True
        return check


