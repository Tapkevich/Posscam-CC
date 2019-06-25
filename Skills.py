import BaseStats
import csv


class SkillEffect(object):
    def __init__(self, key):
        self.key = key
        self.targettype = str
        self.targetamount = str
        self.effecttype = str
        self.damagetype = str
        self.hitchance = float()
        self.critchance = float()
        self.weaponmulty = float()
        self.amountparam = str
        self.amountmulti = float()
        self.amountbase = int()
        self.lenght = float()
        self.lengthmulti = float()
        self.legthparam = str

    def get_skill_effect_params(self):
        skill_effects = csv.DictReader(open(BaseStats.skill_effects))
        for e in skill_effects:
            if self.key == e["Key"]:
                self.targettype = e["TargetType"]
                self.targetamount = e["TargetAmount"]
                self.effecttype = e["TypeEffect"]
                self.damagetype = e["TypeDamage"]
                self.hitchance = float(e["ChanceHit"])
                self.critchance = float(e["ChanceCrit"])
                self.weaponmulty = float(e["WeaponPowerMulti"])
                self.amountparam = e["AmountParam"]
                self.amountmulti = float(e["AmountMulti"])
                self.amountbase = int(e["AmountBase"])
                self.lenght = float(e["LengthBase"])
                self.lengthmulti = float(e["LengthMulti"])
                self.legthparam = e["LengthParam"]





class Skill(object):
    def __init__(self, key):
        self.key = key
        self.skill_effects = []
        self.action_cost = int()
        skill_list = csv.DictReader(open(BaseStats.skill_list), restval='ignore')
        for s in skill_list:
            if self.key == s["Key"]:
                self.skill_effects.append(SkillEffect(s["EffectMain"]))
                self.skill_effects.append(SkillEffect(s["EffectSecondary"]))
                self.action_cost = int(s["ActionCost"])
        for c in self.skill_effects:
            c.get_skill_effect_params()

