import csv
import BaseStats
import BaseCreature
import Skills


class MonsterClass(object):
    def __init__(self, key):
        self.key = key
        self.skillist = []

    # Получаем скиллы для классов мобов
    def get_skills(self, skill_source):
        with open(skill_source) as source:
            class_list = csv.DictReader(source)
            for y in class_list:
                if self.key == y["Key"]:
                    self.skillist.append(Skills.Skill(y["Skill1"]))
                    self.skillist.append(Skills.Skill(y["Skill2"]))
                    self.skillist.append(Skills.Skill(y["Skill3"]))
                else:
                    continue

    def print_skills(self):
        print(self.skillist)


class Monster(BaseCreature.Creature, object):
    def __init__(self, key, class_key, base_key):
        BaseCreature.Creature.__init__(self, key)
        self.monster_class = MonsterClass(class_key)
        self.basis = base_key

    def get_main_stats(self, multy_source, base_source):
        stat_multy = csv.DictReader(open(multy_source))
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
        base_stat = csv.DictReader(open(base_source))
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


