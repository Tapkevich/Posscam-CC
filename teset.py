import wx
import random
import Equipment
import csv
import BaseStats
import Mercenaries

def main():
    test_equip = Equipment.EquipmentCommon("jewelry_catalyst_common", "Uncommon", "Le name")
    test_equip_2 = Equipment.EquipmentCommon("jewelry_gasmask_common", "Common")
    print(test_equip.stat_bonuses["Technic"])
    print(test_equip.name)
    print(test_equip.key)

    test_merc = Mercenaries.Mercenary("chemist_base", "apperance_chemist_common", "Common", "Test subject")
    Mercenaries.MercenaryEquipment.equip_item(test_equip, test_merc)
    Mercenaries.MercenaryEquipment.equip_item(test_equip_2, test_merc, 1)

    for i in test_merc.equiped_items.jewelry:
        if i is None:
            continue
        else:
            print(i.key)

main()