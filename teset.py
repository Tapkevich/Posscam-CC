import wx
import sys
import random
import Equipment
import csv
import BaseStats
import Mercenaries
import Monsters
import Manager

# def main():
    # merc_storage = Manager.MercenaryStorage()
    # item_storage = Manager.ItemStorage()
    # test_equip = Equipment.EquipmentCommon("armor_chem_rare", "Rare", "Le name")
    # test_equip_2 = Equipment.EquipmentCommon("jewelry_gasmask_common", "Common")
    # # print(test_equip.stat_bonuses["ResChem"])
    # # print(test_equip.name)
    # # print(test_equip.key)
    #
    # test_merc = Mercenaries.Mercenary("chemist_base", "apperance_chemist_common", "Common", "Test subject", 20)
    # Mercenaries.MercenaryEquipment.equip_item(test_equip, test_merc)
    # Mercenaries.MercenaryEquipment.equip_item(test_equip_2, test_merc, 1)
    #
    # item_storage.load_common_items()
    # item_storage.load_unique_items()
    #
    # for key, item in item_storage.item_dict.items():
    #     if isinstance(item, Equipment.EquipmentCommon):
    #         item.get_common_equip_base_stats()
    #         print(item.key)
    #         print(item.stat_bonuses)
    #     elif isinstance(item, Equipment.EquipmentUnique):
    #         print(item.key)
    #         print(item.stat_bonuses)
    # item_storage.load_mods()
    # for key, mod in item_storage.mod_dict.items():
    #     print(mod.bonus_dict)

    #
    # print(test_merc.equiped_items.armor.stat_bonuses)
    # for i in test_merc.equiped_items.jewelry:
    #     if i is not None:
    #         print(i.stat_bonuses)
    #
    # # print(test_merc.equiped_items.total_stat_bonus)
    # test_merc.get_equiped_merc_stats()
    # print(test_merc.creature_stats)
    # print(test_merc.rarity)

    # merc_storage.get_available_merc_base_classes()
    # #
    # for t in merc_storage.merc_class_trees:
    #     print(t.show())


    # test_monster = Monsters.Monster("grunt_melee_1", "grunt_melee", "grunt_melee_common")
    # print(test_monster.creature_stats)

#

def main():

    players = [('Tendulkar', '15000', '100'), ('Dravid', '14000', '1'),
               ('Kumble', '1000', '700'), ('KapilDev', '5000', '400'),
               ('Ganguly', '8000', '50')]

    class Mywin(wx.Frame):

        def __init__(self, parent, title):
            super(Mywin, self).__init__(parent, title=title)

            panel = wx.Panel(self)
            box = wx.BoxSizer(wx.HORIZONTAL)

            self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT)
            self.list.InsertColumn(0, 'name', width=100)
            self.list.InsertColumn(1, 'runs', wx.LIST_FORMAT_RIGHT, 100)
            self.list.InsertColumn(2, 'wkts', wx.LIST_FORMAT_RIGHT, 100)

            for i in players:
                index = self.list.InsertStringItem(sys.maxsize, i[0])
                self.list.SetStringItem(index, 1, i[1])
                self.list.SetStringItem(index, 2, i[2])

            box.Add(self.list, 1, wx.EXPAND)
            panel.SetSizer(box)
            panel.Fit()
            self.Centre()

            self.Show(True)

    ex = wx.App()
    Mywin(None, 'ListCtrl Demo')
    ex.MainLoop()

main()