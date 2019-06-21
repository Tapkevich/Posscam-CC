import csv
import itertools

# Таблички
monster_baseparam = "Csv/PSC Data - MonsterBaseParam.csv"
monster_class = "Csv/PSC Data - MonsterClass.csv"

class SkillEffect(object):
    def __init__(self):
        self.key
        self.targettype
        self.targetamount
        self.effecttype
        self.damagetype
        self.hitchance
        self.critchance
        self.amountparam
        self.amountmulti
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
    def __init__(self):
        self.skilllist = []

class Monster(object):
    def __init__(self, key, strength, dexterity, endurance, speed, technic, resphys, resthermo, reschem, dodge):
        self.key = key
        self.strength = strength
        self.dexterity = dexterity
        self.endurance = endurance
        self.speed = speed
        self.technic = technic
        self.resphys = resphys
        self.resthermo = resthermo
        self.reschem = reschem
        self.dodge = dodge
        self.mclass = "None"

    def get_key(self):
        print(self.key)
        print(self.strength)


class MonsterGenerator(object):
    def __init__(self):
        pass

    def create_monsters(self, param_source):
        monster_list = []
        with open(param_source, newline='') as source:
            base_params = csv.DictReader(source, delimiter=',')
            for y in base_params:
                monster_list.append(Monster(y["Key"], y["StatStrength"], y["StatDexterity"], y["StatEndurance"],
                                            y["StatSpeed"], y["StatTechnic"], y["StatResPhys"], y["StatResThermo"],
                                            y["StatResChem"], y["StatDodgeChance"]))
        return monster_list

class MonsterStorage(object):
    def __init__(self, monsters):
        self.monster_list = []

    def get_monsters(self, monster_list):
        self.monster_list = monster_list


test = MonsterGenerator()
test.create_monsters(monster_baseparam)