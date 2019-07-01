import BaseStats
# Базовый класс персонажа, используется, как для мобов так и для чуваков игрока

class Creature(object):
    def __init__(self):
        # Базовые статы
        self.creature_stats = {
            "Strength": 0,
            "Dexterity": 0,
            "Endurance": 0,
            "Technic": 0,
            "Speed": 0,
            "HitChance": 0,
            "CritBonus": 0,
            "DodgeChance": 0,
            "DebuffEfficiency": 0,
            "ResPhys": 0,
            "PhysDmgRed": 0,
            "ResChem": 0,
            "ChemDmgRed": 0,
            "ResThermo": 0,
            "ThermDmgRed": 0,
            "Heal": 0,
            "Power": 0,
            "ActionMod": 0,
            "Health": 0
        }




    def get_key(self):
        print(self.key)