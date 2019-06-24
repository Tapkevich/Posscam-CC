import csv
import BaseStats
import itertools

class SkillEffect(object):
    def __init__(self):
        self.key
        self.targettype = "None"
        self.targetamount = "None"
        self.effecttype = "None"
        self.damagetype = "None"
        self.hitchance = int()
        self.critchance = float()
        self.amountparam = "None"
        self.amountmulti = float()
        self.amountbase = 0
        self.lenghtbase = 0
        self.lengthmulti
        self.legthparam

class Skill(object):
    def __init__(self):
        self.key
        self.skilleffects = []
        self.actioncost


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
                    self.skillist.append(y["Skill1"])
                    self.skillist.append(y["Skill2"])
                    self.skillist.append(y["Skill3"])
                else:
                    continue

    def print_skills(self):
        print(self.skillist)


class Creature(object):
    def __init__(self, key):
        self.key = key
        # Базовые статы
        self.strength = float()
        self.dexterity = float()
        self.endurance = float()
        self.speed = float()
        self.technic= float()
        self.resphys = float()
        self.resthermo = float()
        self.reschem = float()
        self.dodge = float()

    def get_key(self):
        print(self.key)


class Monster(Creature, object):
    def __init__(self, key, class_key, base_key):
        Creature.__init__(self, key)
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

    #def get_secondary_stats(self):

class MonsterGenerator(object):
    def __init__(self):
        pass

    def create_monsters(self, monster_csv, base_csv):
        monster_list = []
        # Создаем по объекту монстра для каждой строки в таблице Monster_final_params.
        with open(monster_csv, newline='') as monster_source:
            monsters = csv.DictReader(monster_source, delimiter=',')
            for y in monsters:
                monster_list.append(Monster(y["Key"], y["Class"], y["Base"]))

        # Даем мобам скиллы
        for m in monster_list:
            m.monster_class.get_skills(BaseStats.monster_class)

        # Даем мобам основные статы.
        for m in monster_list:
            m.get_main_stats(monster_csv, base_csv)

        return monster_list


class MonsterStorage(object):
    def __init__(self):
        self.monster_list = []

    def get_monsters(self, monster_list):
        self.monster_list = monster_list


monster_storage = MonsterStorage()
monster_storage.get_monsters(MonsterGenerator().create_monsters(BaseStats.monster_keys, BaseStats.monster_base_param))

print(monster_storage.monster_list[1].strength)
