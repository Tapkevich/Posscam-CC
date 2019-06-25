import BaseCreature
import BaseStats
import csv

class MercenaryClass(object):
    def __init__(self, key):
        self.key = key
        self.merc_class_skill_list = []
        self.merc_class_phys_res = int()
        self.merc_class_therm_res = int()
        self.merc_class_chem_res = int()
        self.merc_class_dodge = int()
        self.merc_weapon_type = str
        self.merc_talisman_cap = int()

        skill_source = csv.DictReader(open(BaseStats.merc_class))
        for row in skill_source:
            if len(row["Key"]) == 0:
                continue
            elif self.key == row["Key"]:
                self.merc_class_skill_list.append(row["Skill1"])
                self.merc_class_skill_list.append(row["Skill2"])
                self.merc_class_skill_list.append(row["Skill3"])
                self.merc_class_phys_res = int(row["AmountResPhys"])
                self.merc_class_chem_res = int(row["AmountResChem"])
                self.merc_class_therm_res = int(row["AmountResTherm"])
                self.merc_class_dodge = int(row["AmountDodgeChance"])
                self.merc_weapon_type = row ["ClassWeapon"]
                self.merc_talisman_cap = int(row["TalismanAmount"])

class Mercenaries(object):
    def __init__(self, key):
        BaseCreature.Creature.__init__(key)
        self.mercenary_class = MercenaryClass(key)

