import csv
# -------------------------------------------------------------------------------

# Тут хранятся все глобальные переменные и константы, а также ссылки на таблички

# -------------------------------------------------------------------------------

# Таблички c данными баланса
MONSTER_BASE_PARAM_CSV = "Csv/PSC Data - MonsterBaseParam.csv"
MONSTER_CLASS_CSV = "Csv/PSC Data - MonsterClass.csv"
MONSTER_KEYS_CSV = "Csv/PSC Data - MonsterFinallParam.csv"
SKILL_EFFECTS_CSV = "Csv/PSC Data - SkillEffects.csv"
SKILL_LIST_CSV = "Csv/PSC Data - SkillList.csv"
BASE_STATS_CSV = "Csv/PSC Data - BaseStats.csv"  # Тут хранятся разные константные значения
MERC_CLASS_CSV = "Csv/PSC Data - CharacterClass.csv"
MERC_APPERANCE_CSV = "Csv/PSC Data - CharacterAppearance.csv"
MERC_RARITY_COEF_CSV = "CSV/PSC Data - CharacterRarityParam.csv"
ITEM_RARITY_COEF_CSV = "Csv/PSC Data - EquipmentRarityMulti.csv"
ITEM_COMMON_BASES_CSV = "Csv/PSC Data - EquipmentCommon.csv"
ITEM_UNIQUE_STATS_CSV = "Csv/PSC Data - EquipmentUniqueStats.csv"
ITEM_UNIQUE_KEYS = "Csv/PSC Data - EquipmentUniqueKeys.csv"
CRAFT_MODS_BONUSES = "Csv/PSC Data - CraftMods.csv"

# Таблички в которых хранятся локальные предметы
COMMON_ITEMS_STORAGE = "Storage/Common_items.csv"
UNIQUE_ITEMS_STORAGE = "Storage/Unique_items.csv"


# Возможные редкости

RARITY_LIST = [
    "Common",
    "Uncommon",
    "Rare",
    "Epic",
    "Legendary",
    "SupaLegendary"
]

class ConHolder:
    @staticmethod
    def get_constants():
        constants = {}
        temp_dir = csv.DictReader(open(BASE_STATS_CSV))
        for n in temp_dir:
            constants.update({n["Key"]: float(n["Value"])})
        return constants