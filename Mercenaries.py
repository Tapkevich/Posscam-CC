import BaseCreature
import BaseStats
import Equipment
import Skills
import csv


class MercClass(object):
    def __init__(self, key):
        self.key = key
        self.merc_class_skill_list = []
        skill_source = csv.DictReader(open(BaseStats.MERC_CLASS_CSV))
        for row in skill_source:
            if len(row["Key"]) == 0:
                continue
            elif self.key == row["Key"]:
                self.merc_class_skill_list.append(Skills.Skill(row["Skill1"]))
                self.merc_class_skill_list.append(Skills.Skill(row["Skill2"]))
                self.merc_class_skill_list.append(Skills.Skill(row["Skill3"]))
                self.merc_class_phys_res = int(row["ResAmountResPhys"])
                self.merc_class_chem_res = int(row["ResAmountResChem"])
                self.merc_class_therm_res = int(row["ResAmountResThermo"])
                self.merc_class_dodge = int(row["AmountDodgeChance"])
                self.merc_weapon_type = row["ClassWeapon"]
                self.merc_talisman_cap = int(row["TalismanAmount"])


class MercApperance(object):
    def __init__(self, key):
        self.key = key
        apperance_source = csv.DictReader(open(BaseStats.MERC_APPERANCE_CSV))
        for row in apperance_source:
            if len(row["Key"]) == 0:
                continue
            elif self.key == row["Key"]:
                self.available_merc_class = MercClass(row["Class"])
                self.chance_strength = float(row["ChanceStrength"])
                self.chance_dexterity = float(row["ChanceDexterity"])
                self.chance_endurance = float(row["ChanceEndurance"])
                self.chance_technic = float(row["ChanceTechnic"])
                self.chance_speed = float(row["ChanceSpeed"])


class MercRarity(object):
    def __init__(self, key):
        self.key = key
        self.start_point_amount = int()
        self.point_per_level = float()

        source = csv.DictReader(open(BaseStats.MERC_RARITY_COEF_CSV))
        for row in source:
            if len(row["CharacterRarity"]) == 0:
                continue
            elif self.key == row["CharacterRarity"]:
                self.start_point_amount = int(row["PointsAmount"])
                self.point_per_level = float(row["PointsPerLevel"])


class Mercenary(BaseCreature.Creature):
    def __init__(self, merc_class_key, merc_apper_key, merc_rarity, name="None", lvl=1):
        BaseCreature.Creature.__init__(self)
        self.id = int()
        self.level = lvl
        self.name = name
        self.mercenary_class = MercClass(merc_class_key)
        self.rarity = MercRarity(merc_rarity)
        self.apperance = MercApperance(merc_apper_key)
        self.equiped_items = MercenaryEquipment()

    def get_merc_base_stats(self):

        start_points_amount = self.rarity.start_point_amount
        points_per_level = self.rarity.point_per_level
        total_points_amount = start_points_amount + points_per_level*self.level

        self.creature_stats["Strength"] = round(total_points_amount*self.apperance.chance_strength)
        self.creature_stats["Dexterity"] = round(total_points_amount*self.apperance.chance_dexterity)
        self.creature_stats["Endurance"] = round(total_points_amount*self.apperance.chance_endurance)
        self.creature_stats["Speed"] = round(total_points_amount*self.apperance.chance_speed)
        self.creature_stats["Technic"] = round(total_points_amount * self.apperance.chance_technic)
        self.creature_stats["ResChem"] = self.mercenary_class.merc_class_chem_res
        self.creature_stats["ResThermo"] = self.mercenary_class.merc_class_therm_res
        self.creature_stats["ResPhys"] = self.mercenary_class.merc_class_therm_res

    def get_equiped_merc_stats(self):
        self.get_merc_base_stats()
        for key, value in self.creature_stats.items():
            if key in self.equiped_items.total_stat_bonus and self.creature_stats[key] != 0:
                self.creature_stats[key] += self.equiped_items.total_stat_bonus[key]
        self.creature_stats["Power"] += self.equiped_items.total_stat_bonus["Power"]
        self.get_merc_secondary_stats()

    def get_merc_secondary_stats(self):
        self.creature_stats["ChemDmgRed"] = 1/(self.creature_stats["ResChem"] * BaseStats.ConHolder.get_constants().get("ResInfluence") + 1)
        self.creature_stats["PhysDmgRed"] = 1/(self.creature_stats["ResPhys"] * BaseStats.ConHolder.get_constants().get("ResInfluence") + 1)
        self.creature_stats["ThermDmgRed"] = 1/(self.creature_stats["ResThermo"] * BaseStats.ConHolder.get_constants().get("ResInfluence") + 1)

        self.creature_stats["Health"] = self.creature_stats["Endurance"] * BaseStats.ConHolder.get_constants().get("EnduranceHpBonus")

        self.creature_stats["ActionMod"] = (self.creature_stats["Strength"] + self.creature_stats["Endurance"] +
                                            self.creature_stats["Technic"] + self.creature_stats["Dexterity"]) / BaseStats.ConHolder.get_constants().get("SkillCdSpeedMod")

        min_action_mod = float(BaseStats.ConHolder.get_constants().get("CdSpeedInfluenceMin"))
        max_action_mod = float(BaseStats.ConHolder.get_constants().get("CdSpeedInfluenceMax"))
        if self.creature_stats["ActionMod"] <= min_action_mod:
            self.creature_stats["ActionMod"] = min_action_mod
        elif self.creature_stats["ActionMod"] >= max_action_mod:
            self.creature_stats["ActionMod"] = max_action_mod

        self.creature_stats["CritBonus"] = self.creature_stats["Dexterity"] * BaseStats.ConHolder.get_constants().get("DexCritInfluence")\
                                           + self.equiped_items.total_stat_bonus["Crit"]
        self.creature_stats["DodgeChance"] = self.creature_stats["Speed"] * BaseStats.ConHolder.get_constants().get("SpeedDodgeInfluence") + \
                                              self.equiped_items.total_stat_bonus["DodgeChance"]
        self.creature_stats["HitChance"] = self.creature_stats["Dexterity"] * BaseStats.ConHolder.get_constants().get("DexHitInfluence") + \
                                           self.equiped_items.total_stat_bonus["HitChance"]


class MercenaryEquipment(object):
    def __init__(self):
        self.armor = None
        self.weapon = None
        self.jewelry = [None, None]
        self.total_stat_bonus = {
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

    @staticmethod
    def equip_item(item, merc_name, jewelry_slot=0):

        equiped_item_slot = item.slot

        if equiped_item_slot == "Weapon":
            MercenaryEquipment.equip_weapon(item, merc_name)

        if equiped_item_slot == "Armor":
            MercenaryEquipment.equip_armor(item, merc_name)

        if equiped_item_slot == "Jewelry":
            for i in merc_name.equiped_items.jewelry:
                if i is None:
                    continue
                elif i.type == item.type:
                    return "Tried to add same type jewelry"

            MercenaryEquipment.equip_jewelry(item, merc_name, jewelry_slot)

    @staticmethod
    def equip_armor(item, merc_name):

        if merc_name.equiped_items.armor is not None:

            removed_item = merc_name.equiped_items.armor

            for key, value in merc_name.equiped_items.total_stat_bonus.items():
                merc_name.equiped_items.total_stat_bonuses[key] -= removed_item.stat_bonuses[key]
                merc_name.equiped_items.total_stat_bonuses[key] += item.stat_bonuses[key]
        else:
            for key, value in merc_name.equiped_items.total_stat_bonus.items():
                merc_name.equiped_items.total_stat_bonus[key] += item.stat_bonuses[key]

        merc_name.equiped_items.armor = item

    @staticmethod
    def equip_weapon(item, merc_name):
            if merc_name.equiped_items.weapon is not None:
                removed_item = merc_name.equiped_items.weapon
                for key, value in merc_name.equiped_items.total_stat_bonuses.items():
                    merc_name.equiped_items.total_stat_bonuses[key] -= removed_item.stat_bonuses[key]
                    merc_name.equiped_tems.total_stat_bonuses[key] += item.stat_bonuses[key]
            else:
                for key, value in merc_name.equiped_items.total_stat_bonuses:
                    merc_name.equiped_tems.total_stat_bonuses[key] += item.stat_bonuses[key]

            merc_name.equiped_items.weapon = item

    @staticmethod
    def equip_jewelry(item, merc_name, jewelry_slot):

        if merc_name.equiped_items.jewelry[jewelry_slot] is not None:
            removed_item = merc_name.equiped_items.jewelry[jewelry_slot]
            for key, value in merc_name.equiped_items.total_stat_bonus.items():
                merc_name.equiped_items.total_stat_bonus[key] -= removed_item.stat_bonuses[key]
                merc_name.equiped_items.total_stat_bonus[key] += item.stat_bonuses[key]
        else:
            for key, value in merc_name.equiped_items.total_stat_bonus.items():
                merc_name.equiped_items.total_stat_bonus[key] += item.stat_bonuses[key]

        merc_name.equiped_items.jewelry[jewelry_slot] = item




