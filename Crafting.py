import csv
import BaseStats

class CraftMod(object):
    def __init__(self, key):
        self.key = key
        self.bonus_dict = {}
        param_source = csv.DictReader(open(BaseStats.CRAFT_MODS_BONUSES))
        for row in param_source:
            if row["Key"] == self.key:
                if row["Param1"] != "None":
                    self.bonus_dict[row["Param1"]] = row["Amount1"]
                if row["Param2"] != "None":
                    self.bonus_dict[row["Param2"]] = row["Amount2"]
                if row["Param3"] != "None":
                    self.bonus_dict[row["Param3"]] = row["Amount3"]



