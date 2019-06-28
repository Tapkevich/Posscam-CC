import BaseStats
import Manager
import Interface
import wx






def main():
    # monster_storage = Manager.MonsterStorage()
    # monster_storage.get_monsters(Manager.MonsterGenerator().create_monsters())
    # for m in monster_storage.monster_list:
    #     temp_list = m.get_monster_skills()
    #     for s in temp_list:
    #         if len(s.key) == 0:
    #             continue
    #         else:
    #             print(s.key)
    # print(monster_storage.monster_list[1].get_monster_skills())

    # merc_storage = Manager.MercenaryStorage()
    # test_merc = Manager.MercenaryGenerator().create_merc("chemist_base", "apperance_chemist_common", "Common", "TestSubject")
    # merc_storage.add_merc(test_merc)
    #
    # for m in merc_storage.mercenary_list:
    #     print(m.name)
    #     print(m.mercenary_class.key)
    #     print(m.mercenary_class.merc_class_skill_list[2].key)
    #     print(m.mercenary_class.merc_class_phys_res)
    #     print(m.apperance.chance_strength)
    #     print(m.rarity.key)
    #     print(m.rarity.start_point_amount)

    app = wx.App()
    main_menu = Interface.FirstLayer(None, "Combat calc")
    main_menu.Show()
    app.MainLoop()




if __name__ == '__main__':
    main()