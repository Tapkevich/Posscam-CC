import BaseStats
import csv


class SkillEffect(object):
    def __init__(self, key):
        self.key = key
        skill_effects = csv.DictReader(open(BaseStats.SKILL_EFFECTS_CSV))
        for e in skill_effects:
            if len(e["Key"]) == 0:
                continue
            elif self.key == e["Key"]:
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
        skill_list = csv.DictReader(open(BaseStats.SKILL_LIST_CSV), restval='ignore')
        for s in skill_list:
            if len(s["Key"]) == 0:
                continue

            elif self.key == s["Key"]:
                self.skill_effects.append(SkillEffect(s["EffectMain"]))
                self.skill_effects.append(SkillEffect(s["EffectSecondary"]))
                self.action_cost = int(s["ActionCost"])



