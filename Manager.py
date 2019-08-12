import Monsters
import csv
import Mercenaries
import Skills
import BaseCreature
import BaseStats
import treelib
import Equipment as Equip
import ast
import Crafting as Craft

class MonsterStorage(object):
    def __init__(self):
        self.monster_list = []
        self.create_monsters()

    def create_monsters(self):
        monster_list = []
        monster_csv = BaseStats.MONSTER_KEYS_CSV
        # Создаем по объекту монстра для каждой строки в таблице Monster_final_params.
        monsters = csv.DictReader(open(monster_csv))
        for row in monsters:
            monster_list.append(Monsters.Monster(row["Key"], row["Class"], row["Base"]))
        # Считаем второстепенные статы
        for m in monster_list:
            m.set_secondary_stats()

        self.monster_list = monster_list

class MercenaryStorage(object):
    def __init__(self):
        pass
    mercenary_list = []
    merc_class_trees = []

    def get_available_merc_base_classes(self):
        class_source = csv.DictReader(open(BaseStats.MERC_CLASS_CSV))
        for row in class_source:

            class_tree = treelib.Tree()
            main_node = treelib.Node(tag=row["Key"], identifier=row["Key"], data=[row["Master1"], row["Master2"]])

            class_tree.add_node(main_node)
            if row["Master1"] != "None":
                master_1_node = treelib.Node(tag=row["Master1"], identifier=row["Master1"])
                class_tree.add_node(master_1_node, main_node)
            if row["Master2"] != "None":
                master_2_node = treelib.Node(tag=row["Master2"], identifier=row["Master2"])
                class_tree.add_node(master_2_node, main_node)
            if class_tree.size() == 1:
                continue
            else:
                self.merc_class_trees.append(class_tree)

    def add_merc(self, merc):
        self.mercenary_list.append(merc)

    def remove_merc(self, index):
        del self.mercenary_list[index]

    @staticmethod
    def create_merc(merc_class, merc_apperance, merc_rarity, name="Noname"):
        return Mercenaries.Mercenary(merc_class, merc_apperance, merc_rarity, name)


class ItemStorage(object):
    def __init__(self):
        pass
    item_dict = {}
    mod_dict = {}

    def add_item(self, item):
        self.item_dict[item.name] = item

    @staticmethod
    def save_common_item(item):
        fieldnames = ['Key', 'Name', 'Type', 'Slot', "StatBonuses", "Rarity"]
        sniffer = csv.Sniffer()
        csv_dialect = sniffer.sniff(open(BaseStats.MERC_CLASS_CSV).readline())
        writer = csv.DictWriter(open(BaseStats.COMMON_ITEMS_STORAGE, 'a'), fieldnames=fieldnames, dialect=csv_dialect)
        writer.writerow({"Key": item.key, "Name": item.name, "Type": item.type, "Slot": item.slot,
                         "StatBonuses": item.stat_bonuses, "Rarity": item.rarity.key})

    def remove_item(self, item):
        del self.item_dict[item.name]

    def load_common_items(self):
        common_item_source = csv.DictReader(open(BaseStats.COMMON_ITEMS_STORAGE))
        for row in common_item_source:
            new_item = Equip.EquipmentCommon(row["Key"], row["Rarity"], row["Name"])
            new_item.stat_bonuses = ast.literal_eval(row["StatBonuses"])
            new_item.type = row["Type"]
            new_item.slot = row["Slot"]
            self.item_dict[row["Name"]] = new_item

    def load_unique_items(self):
        unique_key_source = csv.DictReader(open(BaseStats.ITEM_UNIQUE_KEYS))
        for row in unique_key_source:
            new_item = Equip.EquipmentUnique(row["Key"], row["Key"])
            self.item_dict[row["Key"]] = new_item

    def load_mods(self):
        mods_source = csv.DictReader(open(BaseStats.CRAFT_MODS_BONUSES))
        for row in mods_source:
            new_mod = Craft.CraftMod(row["Key"])
            # print(new_mod.bonus_dict)
            self.mod_dict[row["Key"]] = new_mod

    def create_item(self, item_key="jewelry_kirpich", item_rarity="Common", item_name="Empty name" ):
        new_item = Equip.EquipmentCommon(item_key, item_name, item_rarity)
        return new_item
















