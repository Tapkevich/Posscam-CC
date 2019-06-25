import csv
# -------------------------------------------------------------------------------

# Тут хранятся все глобальные переменные и константы, а также ссылки на таблички

# -------------------------------------------------------------------------------

# Таблички
monster_base_param = "Csv/PSC Data - MonsterBaseParam.csv"
monster_class = "Csv/PSC Data - MonsterClass.csv"
monster_keys = "Csv/PSC Data - MonsterFinallParam.csv"
skill_effects = "Csv/PSC Data - SkillEffects.csv"
skill_list = "Csv/PSC Data - SkillList.csv"
base_stats = "Csv/PSC Data - BaseStats.csv"


class ConHolder:
    @staticmethod
    def get_constants():
        constants = {}
        temp_dir = csv.DictReader(open(base_stats))
        for n in temp_dir:
            constants.update({n["Key"]: float(n["Value"])})
        return constants

