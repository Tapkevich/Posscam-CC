import BaseStats
import Manager

monster_storage = Manager.MonsterStorage()
monster_storage.get_monsters(Manager.MonsterGenerator().create_monsters(BaseStats.monster_keys,
                                                                        BaseStats.monster_base_param))

# print(monster_storage.monster_list[5].endurance)

