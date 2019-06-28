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
                self.merc_class_phys_res = int(row["AmountResPhys"])
                self.merc_class_chem_res = int(row["AmountResChem"])
                self.merc_class_therm_res = int(row["AmountResThermo"])
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
                self.chacne_technic = float(row["ChanceTechnic"])
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
                self.start_point_amount = row["PointsAmount"]
                self.point_per_level = row["PointsPerLevel"]



class Mercenary(object):
    def __init__(self, merc_class_key, merc_apper_key, merc_rarity, name = "None"):
        BaseCreature.Creature.__init__(self)
        self.id = int()
        self.name = name
        self.mercenary_class = MercClass(merc_class_key)
        self.rarity = MercRarity(merc_rarity)
        self.apperance = MercApperance(merc_apper_key)
        self.equiped_items = MercenaryEquipment()


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
        if equiped_item_slot == "Weapon" and Equipment.EquipmentUtility.check_weapon_type(merc_name, item):
            merc_name.equiped_items.weapon = item

        if equiped_item_slot == "Armor":
            merc_name.equiped_items.armor = item

        if equiped_item_slot == "Jewelry":
            for i in merc_name.equiped_items.jewelry:
                if i is None:
                    continue
                elif i.type == item.type:
                    return "Tried to add s.t jewelry"

            merc_name.equiped_items.jewelry[jewelry_slot] = item

    def get_stat_bonus(self):
        for key, value in self.total_stat_bonus.items():
            if key in self.pohui:
                self.pohui[key] += value
            else:
                self.pohui[key] = value


        if self.armor is not None:
            self.total_stat_bonus["Strength"] += self.armor.stat_bonuses["Strength"]

        if self.weapon is not None:
            self.total_stat_bonus["Strength"] += self.weapon.stat_bonuses["Strength"]

        for i in self.jewelry:
            if i is not None:
                self.total_stat_bonus["Strength"] += i.stat_bonuses["Strength"]



