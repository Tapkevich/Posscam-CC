import wx
import random
import Equipment
import csv
import BaseStats
import Mercenaries
import Monsters


def main():
    test_equip = Equipment.EquipmentCommon("armor_chem_rare", "Rare", "Le name")
    # test_equip_2 = Equipment.EquipmentCommon("jewelry_gasmask_common", "Common")
    # print(test_equip.stat_bonuses["ResChem"])
    # print(test_equip.name)
    # print(test_equip.key)
    #
    # test_merc = Mercenaries.Mercenary("chemist_base", "apperance_chemist_common", "Common", "Test subject")
    # Mercenaries.MercenaryEquipment.equip_item(test_equip, test_merc)
    # Mercenaries.MercenaryEquipment.equip_item(test_equip_2, test_merc, 1)
    #
    # print(test_merc.equiped_items.armor.stat_bonuses)
    # for i in test_merc.equiped_items.jewelry:
    #     if i is not None:
    #         print(i.stat_bonuses)
    #
    # print(test_merc.equiped_items.total_stat_bonus)

    test_monster = Monsters.Monster("grunt_melee_1", "grunt_melee", "grunt_melee_common")
    print(test_monster.creature_stats)


main()