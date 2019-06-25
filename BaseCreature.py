import BaseStats
# Базовый класс персонажа, используется, как для мобов так и для чуваков игрока

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
        self.weaponpower = float()

        #Второстепенные статы
        self.damagereduction = float()
        self.hitpoints = int()
        self.action_mod = float()
        self.efficiency = float()
        self.healpower = float()
        self.reductionphys = float()
        self.reductionthermo = float()
        self.reductionchem = float()
        self.critchancebonus = float()

    def set_secondary_stats(self):
        self.reductionchem = 1/(self.reschem * BaseStats.ConHolder.get_constants().get("ResInfluence") + 1)
        self.reductionphys = 1/(self.resphys * BaseStats.ConHolder.get_constants().get("ResInfluence") + 1)
        self.reductionthermo = 1/(self.resthermo * BaseStats.ConHolder.get_constants().get("ResInfluence") + 1)
        self.hitpoints = self.endurance * BaseStats.ConHolder.get_constants().get("EnduranceHpBonus")
        self.action_mod = (self.strength + self.endurance + self.technic +
                           self.dexterity) / BaseStats.ConHolder.get_constants().get("SkillCdSpeedMod")

        min_action_mod = float(BaseStats.ConHolder.get_constants().get("CdSpeedInfluenceMin"))
        max_action_mod = float(BaseStats.ConHolder.get_constants().get("CdSpeedInfluenceMax"))
        if self.action_mod <= min_action_mod:
            self.action_mod = min_action_mod
        elif self.action_mod >= max_action_mod:
            self.action_mod = max_action_mod
        else:

            pass

        self.efficiency = 1
        self.healpower = 1
        self.critchancebonus = self.dexterity * BaseStats.ConHolder.get_constants().get("DexCritInfluence")




    def get_key(self):
        print(self.key)