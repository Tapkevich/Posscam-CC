import csv
import itertools

# Таблички
monster_base_param = "Csv/PSC Data - MonsterBaseParam.csv"
monster_class = "Csv/PSC Data - MonsterClass.csv"
monster_keys = "Csv/PSC Data - MonsterFinallParam.csv"

# class SkillEffect(object):
#     def __init__(self):
#         self.key
#         self.targettype
#         self.targetamount
#         self.effecttype
#         self.damagetype
#         self.hitchance
#         self.critchance
#         self.amountparam
#         self.amountmulti
#         self.amountbase = 0
#         self.lenghtbase = 0
#         self.lengthmulti
#         self.legthparam
#
#
#
#
# class Skill(object):
#     def __init__(self):
#         self.key
#         self.skilleffects = []
#         self.actioncost
#
class Monster_basis(object):
    def __init__(self, key):
        self.key = key

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


class Monster(object):
    def __init__(self, key, strength, dexterity, endurance, speed, technic, resphys, resthermo, reschem, dodge,
                 base_key, class_key):
        self.key = key
        self.monster_class = MonsterClass(class_key)
        self.basis = Monster_basis(base_key)
        # Статы мобов
        self.strength = strength
        self.dexterity = dexterity
        self.endurance = endurance
        self.speed = speed
        self.technic= technic
        self.resphys = resphys
        self.resthermo = resthermo
        self.reschem = reschem
        self.dodge = dodge

    def get_key(self):
        print(self.key)


class MonsterGenerator(object):
    def __init__(self):
        pass

    def create_monsters(self, param_source):
        monster_list = []
        # Создаем по объекту монстра для каждой строки в таблице Monster_final_params.
        with open(param_source, newline='') as source:
            base_params = csv.DictReader(source, delimiter=',')
            for y in base_params:
                monster_list.append(Monster(y["Key"], y["MultiStrength"], y["MultiDexterity"], y["MultiEndurance"],
                                            y["MultiSpeed"], y["MultiTechnic"], y["MultiResPhys"], y["MultiResThermo"],
                                            y["MultiResChem"], y["MultiDodgeChance"], y["Class"], y["Base"]))
        for m in monster_list:
            m.monster_class.get_skills(monster_class)

        return monster_list

class MonsterStorage(object):
    def __init__(self):
        self.monster_list = []

    def get_monsters(self, monster_list):
        self.monster_list = monster_list


monster_storage = MonsterStorage()
monster_storage.get_monsters(MonsterGenerator().create_monsters(monster_keys))

for m in monster_storage.monster_list:
    m.monster_class.print_skills

