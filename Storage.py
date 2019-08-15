import csv
import BaseStats
import ast
import json
import Equipment as Equip
import Crafting as Craft


class ItemStorage(object):
    def __init__(self):
        pass
    item_dict = {}
    mod_dict = {}

    @staticmethod
    def add_item(item):
        item_storage.item_dict[item.name] = item

    @staticmethod
    def save_common_item(item):
        item_mod_keys = []
        for mod in item.mod_list:
            item_mod_keys.append(mod.key)

        fieldnames = ['Key', 'Name', 'Type', 'Slot', "ModList", "Rarity"]
        sniffer = csv.Sniffer()
        csv_dialect = sniffer.sniff(open(BaseStats.MERC_CLASS_CSV).readline())
        writer = csv.DictWriter(open(BaseStats.COMMON_ITEMS_STORAGE, 'a'), fieldnames=fieldnames, dialect=csv_dialect, escapechar='\\')
        writer.writerow({"Key": item.key, "Name": item.name, "Type": item.type, "Slot": item.slot,
                         "ModList": json.dumps(item_mod_keys), "Rarity": item.rarity.key})

    @staticmethod
    def remove_item(item):
        del item_storage.item_dict[item.name]

    @staticmethod
    def load_common_items():
        common_item_source = csv.DictReader(open(BaseStats.COMMON_ITEMS_STORAGE), escapechar='\\')
        for row in common_item_source:
            new_item = Equip.EquipmentCommon(row["Key"], row["Rarity"], row["Name"])

            new_item.mod_list = []
            mod_list_keys = json.loads(row["ModList"])
            for m in mod_list_keys:
                for key, value in item_storage.mod_dict.items():
                    if key == m:
                        new_item.mod_list.append(value)
            new_item.get_total_rand_stats()

            new_item.type = row["Type"]
            new_item.slot = row["Slot"]
            item_storage.item_dict[row["Name"]] = new_item

    @staticmethod
    def get_common_item_keys():
        stat_source = csv.DictReader(open(BaseStats.ITEM_COMMON_BASES_CSV))
        item_keys = []
        for row in stat_source:
            item_keys.append(row["Key"])
        return item_keys

    @staticmethod
    def load_unique_items():
        unique_key_source = csv.DictReader(open(BaseStats.ITEM_UNIQUE_KEYS))
        for row in unique_key_source:
            new_item = Equip.EquipmentUnique(row["Key"], row["Key"])
            item_storage.item_dict[row["Key"]] = new_item

    @staticmethod
    def load_mods():
        mods_source = csv.DictReader(open(BaseStats.CRAFT_MODS_BONUSES))
        for row in mods_source:
            new_mod = Craft.CraftMod(row["Key"])
            # print(new_mod.bonus_dict)
            item_storage.mod_dict[row["Key"]] = new_mod




item_storage = ItemStorage()
item_storage.load_mods()
item_storage.load_common_items()

