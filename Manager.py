import Monsters
import csv
import Mercenaries
import Skills
import BaseCreature
import BaseStats

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
        self.mercenary_list = []

    def add_merc(self, merc):
        self.mercenary_list.append(merc)

    def remove_merc(self, index):
        del self.mercenary_list[index]

    @staticmethod
    def create_merc(merc_class, merc_apperance, merc_rarity, name="Noname"):
        return Mercenaries.Mercenary(merc_class, merc_apperance, merc_rarity, name)

