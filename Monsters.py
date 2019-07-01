import csv
import BaseStats
import BaseCreature
import Skills


class MonsterClass(object):
    def __init__(self, key):
        self.key = key
        self.skillist = []
        monster_skill_csv = csv.DictReader(open(BaseStats.MONSTER_CLASS_CSV))
        for row in monster_skill_csv:
            if len(row["Key"])== 0:
                continue
            elif row["Key"] == self.key:
                self.skillist.append(Skills.Skill(row["Skill1"]))
                self.skillist.append(Skills.Skill(row["Skill2"]))
                self.skillist.append(Skills.Skill(row["Skill3"]))


class Monster(BaseCreature.Creature, object):
    def __init__(self, key, class_key, base_key):
        BaseCreature.Creature.__init__(self)
        self.key = key
        self.monster_class = MonsterClass(class_key)
        self.basis = base_key
        self.get_monster_stats()

    def get_monster_stats(self):
        stat_multy = csv.DictReader(open(BaseStats.MONSTER_KEYS_CSV))
        for m in stat_multy:
            if self.key == m["Key"]:
                self.creature_stats["Strength"] = float(m["MultiStrength"])
                self.creature_stats["Dexterity"] = float(m["MultiDexterity"])
                self.creature_stats["Endurance"] = float(m["MultiEndurance"])
                self.creature_stats["Speed"] = float(m["MultiSpeed"])
                self.creature_stats["Technic"] = float(m["MultiTechnic"])
                self.creature_stats["ResPhys"] = float(m["MultiResPhys"])
                self.creature_stats["ResThermo"] = float(m["MultiResThermo"])
                self.creature_stats["ResChem"] = float(m["MultiResChem"])
                self.creature_stats["DodgeChance"] = float(m["MultiDodgeChance"])
            else:
                continue

        base_stat = csv.DictReader(open(BaseStats.MONSTER_BASE_PARAM_CSV))
        for m in base_stat:
            if self.basis == m["Key"]:
                self.creature_stats["Strength"] = round(self.creature_stats["Strength"] * float(m["StatStrength"]))
                self.creature_stats["Dexterity"] = round(self.creature_stats["Dexterity"] * float(m["StatDexterity"]))
                self.creature_stats["Endurance"] = round(self.creature_stats["Endurance"] * float(m["StatEndurance"]))
                self.creature_stats["Speed"] = round(self.creature_stats["Speed"] * float(m["StatSpeed"]))
                self.creature_stats["Technic"] = round(self.creature_stats["Technic"] * float(m["StatTechnic"]))
                self.creature_stats["ResThermo"] = round(self.creature_stats["ResThermo"] * float(m["StatResThermo"]))
                self.creature_stats["ResChem"] = round(self.creature_stats["ResChem"] * float(m["StatResChem"]))
                self.creature_stats["ResPhys"] = round(self.creature_stats["ResPhys"] * float(m["StatResPhys"]))
                self.creature_stats["DodgeChance"] = round(self.creature_stats["DodgeChance"] * float(m["StatDodgeChance"]))
            else:
                continue
        Monster.set_monster_secondary_stats(self)

    def set_monster_secondary_stats(self):
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

        self.creature_stats["CritBonus"] = self.creature_stats["Dexterity"] * BaseStats.ConHolder.get_constants().get("DexCritInfluence")
        self.creature_stats["DodgeChance"] += self.creature_stats["Speed"] * BaseStats.ConHolder.get_constants().get("SpeedDodgeInfluence")
        self.creature_stats["HitChance"] = self.creature_stats["Dexterity"] * BaseStats.ConHolder.get_constants().get("DexHitInfluence")


