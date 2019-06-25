import Monsters
import csv
import Skills
import BaseCreature
import BaseStats

class MonsterStorage(object):
    def __init__(self):
        self.monster_list = []

    def get_monsters(self, monster_list):
        self.monster_list = monster_list


class MonsterGenerator(object):

    def create_monsters(self, monster_csv, base_csv):
        monster_list = []
        # Создаем по объекту монстра для каждой строки в таблице Monster_final_params.
        with open(monster_csv, newline='') as monster_source:
            monsters = csv.DictReader(monster_source, delimiter=',')
            for y in monsters:
                monster_list.append(Monsters.Monster(y["Key"], y["Class"], y["Base"]))

        # Даем мобам скиллы
        for m in monster_list:
            m.monster_class.get_skills(BaseStats.monster_class)

        # Даем мобам основные статы.
        for m in monster_list:
            m.get_main_stats(monster_csv, base_csv)
        # Считаем второстепенные статы
        for m in monster_list:
            m.set_secondary_stats()

        return monster_list
