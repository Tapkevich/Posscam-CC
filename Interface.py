import wx
import Main
import Manager
import Equipment
import random
import Storage
import BaseStats
import Crafting
APP_EXIT = 1

class MiscFunctions():
    @staticmethod
    def scale_bitmap_image(bitmap, width, height):
        image = bitmap.ConvertToImage()
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result

# Основное меню представляющее из себя набор ввкладок с различным функционалом.
# FirstLayer используется, чтобы связать их вместе.


class FirstLayer(wx.Frame):
    def __init__(self, parent):
        super(FirstLayer, self).__init__(parent)
        self.init_ui()
        self.Centre()

    def init_ui(self):

        # Создаем список вещей для дальнейшего использования во вьюхах

        p = wx.Panel(self)
        nb = wx.Notebook(p)

        page_1 = MainMenu(nb)
        page_2 = CharacterList(nb)
        page_3 = ItemList(nb)

        nb.AddPage(page_1, "MainMenu")
        nb.AddPage(page_2, "Character List")
        nb.AddPage(page_3, "Item list")

        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)

        self.SetTitle('Le calculator')
        self.SetBackgroundColour("GRAY")


class MainMenu(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.ui_stuff()

    def ui_stuff(self):
        pass


class CharacterList(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.ui_init()

    def ui_init(self):
        pass


class ItemList(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.item_list = wx.ListBox(self, -1)
        self.update_item_list()
        self.ui_init()

    def ui_init(self):

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        add_item_button = wx.Button(self, -1, "Add")
        remove_item_button = wx.Button(self, -1, "Remove")
        modify_item_button = wx.Button(self, -1, "Change")

        add_item_button.Bind(wx.EVT_BUTTON, self.add_item)
        modify_item_button.Bind(wx.EVT_BUTTON, self.mod_item)

        some_text = wx.StaticText(self, -1, "ITEM LIBRARY")

        button_sizer.Add(add_item_button, wx.ID_ANY)
        button_sizer.Add(modify_item_button, wx.ID_ANY)
        button_sizer.Add(remove_item_button, wx.ID_ANY)

        main_sizer.Add(some_text, wx.ID_ANY, 0, wx.ALIGN_BOTTOM, 0)
        main_sizer.Add(self.item_list, wx.ID_ANY, wx.EXPAND)
        main_sizer.Add(button_sizer, wx.ID_ANY, flag=wx.EXPAND | wx.BOTTOM, border=5)

        self.SetSizer(main_sizer)

        main_sizer.SetSizeHints(self.item_list)

    def update_item_list(self):
        self.item_list.Clear()
        for key, item in Storage.item_storage.item_dict.items():
            self.item_list.Append(key)

    def add_item(self, e):
        item_info = ItemInfo(None, "Item name")
        self.update_item_list()
        item_info.Show()

    def mod_item(self,e):

        if self.item_list.GetSelection() == -1:
            message = wx.MessageDialog(self, message="You didn't choose a character", caption="Error")
            message.ShowModal()
            message.Destroy()
        else:
            choosed_item = self.item_list.GetString(self.item_list.GetSelection())
            item_info = ItemInfo(None, choosed_item)
            item_info.Show()



class ItemInfo(wx.Frame):
    def __init__(self, parent, item, *args):
        super(ItemInfo, self).__init__(parent)
        self.Centre()
        self.Size = wx.Size(500, 600)

        current_item = self.find_current_item(item)
        common_item_types = Storage.ItemStorage.get_common_item_keys()

        mod_list = []
        mod_list.append("None")
        for key, value in Storage.item_storage.mod_dict.items():
            mod_list.append(key)

        ##================================ Верхний блок ==========================

        self.name_sizer = wx.BoxSizer(wx.VERTICAL)
        self.item_name = wx.StaticText(self, label="Name")
        self.item_type = wx.TextCtrl(self, wx.ID_ANY, item, wx.DefaultPosition)
        self.name_sizer.Add(self.item_name, wx.ID_ANY, wx.ALIGN_CENTER_HORIZONTAL, wx.BOTTOM)
        self.name_sizer.Add(self.item_type, wx.ID_ANY, wx.EXPAND)

        self.item_key_sizer = wx.BoxSizer(wx.VERTICAL)
        self.item_key_label = wx.StaticText(self, label="Item key")
        self.item_key_combobox = wx.ComboBox(self, value=current_item.key, choices=common_item_types)
        self.item_key_sizer.Add(self.item_key_label, wx.ID_ANY, wx.ALIGN_CENTER_HORIZONTAL, wx.BOTTOM)
        self.item_key_sizer.Add(self.item_key_combobox, wx.ID_ANY, wx.EXPAND)

        self.item_rarity_sizer = wx.BoxSizer(wx.VERTICAL)
        self.item_rarity_label = wx.StaticText(self, label="Item rarity")
        self.item_rarity_value = wx.ComboBox(self, value=current_item.rarity.key, choices=BaseStats.RARITY_LIST)
        self.item_rarity_sizer.Add(self.item_rarity_label, wx.ID_ANY, wx.ALIGN_CENTER_HORIZONTAL, wx.BOTTOM)
        self.item_rarity_sizer.Add(self.item_rarity_value, wx.ID_ANY, wx.EXPAND)

        self.required_stats_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.required_stats_sizer.Add(self.name_sizer, wx.ID_ANY, wx.EXPAND, wx.LEFT|wx.RIGHT, 20)
        self.required_stats_sizer.Add(self.item_key_sizer, wx.ID_ANY, wx.EXPAND, wx.LEFT|wx.RIGHT, 20)
        self.required_stats_sizer.Add(self.item_rarity_sizer, wx.ID_ANY, wx.EXPAND, wx.LEFT|wx.RIGHT, 20)

        self.top_sizer = wx.BoxSizer(wx.VERTICAL)

        self.top_label = wx.StaticText(self, label="Main parameters")
        self.top_sizer.Add(self.top_label, wx.ID_ANY, wx.ALIGN_CENTER_HORIZONTAL, wx.BOTTOM, 30)
        self.top_sizer.Add(self.required_stats_sizer, wx.ID_ANY, wx.EXPAND, wx.BOTTOM, 30)

        ##==================Список модов в предмете и контролы для их смены===========
        self.mod_section = wx.BoxSizer(wx.VERTICAL)
        self.item_mods = wx.BoxSizer(wx.HORIZONTAL)

        self.mod_list_label = wx.StaticText(self, label="Item mods")
        self.mod1_combobox = wx.ComboBox(self, value=current_item.mod_list[0].key, choices=mod_list)
        self.mod2_combobox = wx.ComboBox(self, value=current_item.mod_list[1].key, choices=mod_list)
        self.mod3_combobox = wx.ComboBox(self, value=current_item.mod_list[2].key, choices=mod_list)

        self.item_mods.Add(self.mod1_combobox, wx.ID_ANY, wx.EXPAND, wx.LEFT|wx.RIGHT, 50)
        self.item_mods.Add(self.mod2_combobox, wx.ID_ANY, wx.EXPAND, wx.LEFT|wx.RIGHT, 50)
        self.item_mods.Add(self.mod3_combobox, wx.ID_ANY, wx.EXPAND, wx.LEFT|wx.RIGHT, 50)

        self.mod_section.Add(self.mod_list_label, wx.ID_ANY, wx.ALIGN_CENTER_HORIZONTAL, wx.BOTTOM, 20)
        self.mod_section.Add(self.item_mods, wx.ID_ANY, wx.EXPAND)

        ## ============================== Статы предмета ============================

        self.stat_grid_sizer = wx.GridSizer(cols=2, hgap=30, vgap=20)
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"Strength: {current_item.stat_bonuses['Strength']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"Dexterity: {current_item.stat_bonuses['Dexterity']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"Endurance: {current_item.stat_bonuses['Endurance']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"Technic: {current_item.stat_bonuses['Technic']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"Speed: {current_item.stat_bonuses['Speed']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"HitChance: {current_item.stat_bonuses['HitChance']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"Crit: {current_item.stat_bonuses['Crit']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"DodgeChance: {current_item.stat_bonuses['DodgeChance']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"DebuffEfficiency: {current_item.stat_bonuses['DebuffEfficiency']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"ResPhys: {current_item.stat_bonuses['ResPhys']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"ResChem: {current_item.stat_bonuses['ResChem']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"ResThermo: {current_item.stat_bonuses['ResThermo']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"Heal: {current_item.stat_bonuses['Heal']}"))
        self.stat_grid_sizer.Add(wx.StaticText(self, label=f"Power: {current_item.stat_bonuses['Power']}"))




        self.stat_label = wx.StaticText(self, label="Item stats")

        self.stat_sizer = wx.BoxSizer(wx.VERTICAL)
        self.stat_sizer.Add(self.stat_label, wx.ID_ANY, wx.ALIGN_CENTER, wx.BOTTOM, 20)
        self.stat_sizer.Add(self.stat_grid_sizer, wx.ID_ANY, wx.EXPAND, 20)

        ##=============================== Главный сайзер================================
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_sizer.Add(self.top_sizer, wx.ID_ANY, wx.EXPAND, wx.BOTTOM, 20)
        self.main_sizer.Add(self.mod_section, wx.ID_ANY, wx.EXPAND, wx.BOTTOM, 20)
        self.main_sizer.Add(self.stat_sizer, wx.ID_ANY, wx.EXPAND, wx.BOTTOM, 20)

        # self.main_sizer.SetSizeHints(self)
        self.SetSizer(self.main_sizer)

    def find_current_item(self, item):
        common_item_types = Storage.ItemStorage.get_common_item_keys()

        temp_modlist = [Crafting.CraftMod("None"), Crafting.CraftMod("None"), Crafting.CraftMod("None")]

        if item == "Item name":
            current_item = Equipment.EquipmentCommon(random.choice(common_item_types), "Common",
                                                     "Item name", temp_modlist)
        else:
            current_item = Storage.item_storage.item_dict[item]
            print(current_item.stat_bonuses)
        return current_item











