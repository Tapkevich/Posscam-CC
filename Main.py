import BaseStats
import Manager
import Interface
import wx
import Storage
import Crafting
import Equipment
import random



def main():


    # for mods in new_item.mod_list:
    #     print(mods.bonus_dict)

    # Storage.ItemStorage.save_common_item(new_item)


    # for key, value in Storage.item_storage.item_dict.items():
    #     for m in value.mod_list:
    #         print(m.bonus_dict)


    for key, value in Storage.item_storage.item_dict.items():
        print(value.stat_bonuses)
        value.get_mod_bonus_stats()
        print(value.stat_bonuses)
        print(value.rand_amount)

    app = wx.App()
    main_menu = Interface.FirstLayer(None)
    main_menu.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()