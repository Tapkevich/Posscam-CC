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

    def print_skills(self):
        print(self.skillist)


class Monster(BaseCreature.Creature, object):
    def __init__(self, key, class_key, base_key):
        BaseCreature.Creature.__init__(self)
        self.key = key
        self.monster_class = MonsterClass(class_key)
        self.basis = base_key
        stat_multy = csv.DictReader(open(BaseStats.MONSTER_KEYS_CSV))
        for m in stat_multy:
            if self.key == m["Key"]:
                self.strength = float(m["MultiStrength"])
                self.dexterity = float(m["MultiDexterity"])
                self.endurance = float(m["MultiEndurance"])
                self.speed = float(m["MultiSpeed"])
                self.technic = float(m["MultiTechnic"])
                self.resphys = float(m["MultiResPhys"])
                self.resthermo = float(m["MultiResThermo"])
                self.reschem = float(m["MultiResChem"])
                self.dodge = float(m["MultiDodgeChance"])
            else:
                continue
        base_stat = csv.DictReader(open(BaseStats.MONSTER_BASE_PARAM_CSV))
        for m in base_stat:
            if self.basis == m["Key"]:
                self.strength = self.strength * float(m["StatStrength"])
                self.dexterity = self.dexterity * float(m["StatDexterity"])
                self.endurance = self.endurance * float(m["StatEndurance"])
                self.speed = self.speed * float(m["StatSpeed"])
                self.technic = self.technic * float(m["StatTechnic"])
                self.resthermo = self.resthermo * float(m["StatResThermo"])
                self.reschem = self.reschem * float(m["StatResChem"])
                self.resphys = self.resphys * float(m["StatResPhys"])
            else:
                continue

    def get_monster_skills(self):
        return self.monster_class.skillist


