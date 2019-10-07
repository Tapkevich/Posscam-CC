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
        self.Size = wx.Size(500, 700)

        self.current_item = self.find_current_item(item)
        common_item_types = Storage.ItemStorage.get_common_item_keys()

        self.Bind(wx.EVT_SHOW, self.show_current_item_stats)

        mod_list = []
        mod_list.append("None")
        for key, value in Storage.item_storage.mod_dict.items():
            mod_list.append(key)

        ##============================= Шрифты ===============================##

        label_font = wx.Font(16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        sublabel_font = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        stat_font = wx.Font(16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)

        ##================================ Верхний блок ==========================


        self.name_sizer = wx.BoxSizer(wx.VERTICAL)
        self.item_name = wx.StaticText(self, label="Name")
        self.item_name.SetFont(sublabel_font)
        self.item_type = wx.TextCtrl(self, wx.ID_ANY, item, wx.DefaultPosition)
        self.name_sizer.Add(self.item_name, wx.ID_ANY, wx.ALIGN_CENTER_HORIZONTAL, wx.BOTTOM)
        self.name_sizer.Add(self.item_type, wx.ID_ANY, wx.EXPAND)

        self.item_key_sizer = wx.BoxSizer(wx.VERTICAL)
        self.item_key_label = wx.StaticText(self, label="Item key")
        self.item_key_label.SetFont(sublabel_font)
        self.item_key_combobox = wx.ComboBox(self, value=self.current_item.key, choices=common_item_types)
        self.item_key_sizer.Add(self.item_key_label, wx.ID_ANY, wx.ALIGN_CENTER_HORIZONTAL, wx.BOTTOM)
        self.item_key_sizer.Add(self.item_key_combobox, wx.ID_ANY, wx.EXPAND)

        self.item_key_combobox.Bind(wx.EVT_COMBOBOX, self.update_new_item_stats)

        self.item_rarity_sizer = wx.BoxSizer(wx.VERTICAL)
        self.item_rarity_label = wx.StaticText(self, label="Item rarity")
        self.item_rarity_label.SetFont(sublabel_font)
        self.item_rarity_value = wx.ComboBox(self, value=self.current_item.rarity.key, choices=BaseStats.RARITY_LIST)
        self.item_rarity_sizer.Add(self.item_rarity_label, wx.ID_ANY, wx.ALIGN_CENTER_HORIZONTAL, wx.BOTTOM)
        self.item_rarity_sizer.Add(self.item_rarity_value, wx.ID_ANY, wx.EXPAND)

        self.item_rarity_value.Bind(wx.EVT_COMBOBOX, self.update_new_item_stats)

        self.required_stats_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.required_stats_sizer.Add(self.name_sizer, wx.ID_ANY, wx.EXPAND, wx.LEFT|wx.RIGHT, 20)
        self.required_stats_sizer.Add(self.item_key_sizer, wx.ID_ANY, wx.EXPAND, wx.LEFT|wx.RIGHT, 20)
        self.required_stats_sizer.Add(self.item_rarity_sizer, wx.ID_ANY, wx.EXPAND, wx.LEFT|wx.RIGHT, 20)

        self.top_sizer = wx.BoxSizer(wx.VERTICAL)

        self.top_label = wx.StaticText(self, label="Main parameters")
        self.top_label.SetFont(label_font)
        self.top_sizer.Add(self.top_label, wx.ID_ANY, wx.ALIGN_CENTER_HORIZONTAL, wx.BOTTOM, 30)
        self.top_sizer.Add(self.required_stats_sizer, wx.ID_ANY, wx.EXPAND, wx.BOTTOM, 30)

        ##==================Список модов в предмете и контролы для их смены===========
        self.mod_section = wx.BoxSizer(wx.VERTICAL)
        self.item_mods = wx.BoxSizer(wx.HORIZONTAL)

        mod_list_label = wx.StaticText(self, label="Item mods")
        mod_list_label.SetFont(label_font)
        mod1_combobox = wx.ComboBox(self, value=self.current_item.mod_list[0].key, choices=mod_list)
        mod2_combobox = wx.ComboBox(self, value=self.current_item.mod_list[1].key, choices=mod_list)
        mod3_combobox = wx.ComboBox(self, value=self.current_item.mod_list[2].key, choices=mod_list)



        self.item_mods.Add(mod1_combobox, wx.ID_ANY, wx.EXPAND, wx.LEFT|wx.RIGHT, 50)
        self.item_mods.Add(mod2_combobox, wx.ID_ANY, wx.EXPAND, wx.LEFT|wx.RIGHT, 50)
        self.item_mods.Add(mod3_combobox, wx.ID_ANY, wx.EXPAND, wx.LEFT|wx.RIGHT, 50)

        mod1_combobox.Bind(wx.EVT_COMBOBOX, self.update_new_item_stats)
        mod2_combobox.Bind(wx.EVT_COMBOBOX, self.update_new_item_stats)
        mod3_combobox.Bind(wx.EVT_COMBOBOX, self.update_new_item_stats)

        self.mod_section.Add(mod_list_label, wx.ID_ANY, wx.ALIGN_CENTER_HORIZONTAL, wx.BOTTOM, 20)
        self.mod_section.Add(self.item_mods, wx.ID_ANY, wx.EXPAND)

        # Привязываем ивент изменения состояния комбобокса ко всем боксам

        self.mod_boxes = [mod1_combobox, mod2_combobox, mod3_combobox]

        # for m in self.mod_boxes:
        #     m.Bind(wx.EVT_COMBOBOX, self.update_new_item_stats)

        # ============================== Статы предмета ============================

        stat_grid_sizer = wx.GridSizer(cols=3, hgap=30, vgap=20)

        self.str_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.str_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.str_amount_txt)
        self.dex_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.dex_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.dex_amount_txt)
        self.end_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.end_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.end_amount_txt)
        self.tech_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.tech_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.tech_amount_txt)
        self.spd_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.spd_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.spd_amount_txt)
        self.hit_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.hit_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.hit_amount_txt)
        self.crit_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.crit_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.crit_amount_txt)
        self.dodge_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.dodge_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.dodge_amount_txt)
        self.effic_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.effic_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.effic_amount_txt)
        self.resphys_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.resphys_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.resphys_amount_txt)
        self.reschem_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.reschem_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.reschem_amount_txt)
        self.restherm_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.restherm_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.restherm_amount_txt)
        self.heal_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.heal_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.heal_amount_txt)
        self.power_amount_txt = wx.StaticText(self, label="Didn't get stats")
        self.power_amount_txt.SetFont(stat_font)
        stat_grid_sizer.Add(self.power_amount_txt)

        stat_label = wx.StaticText(self, label="Item stats")
        stat_label.SetFont(label_font)
        self.stat_sizer = wx.BoxSizer(wx.VERTICAL)
        self.stat_sizer.Add(stat_label, wx.ID_ANY, wx.ALIGN_CENTER, wx.BOTTOM, 20)
        self.stat_sizer.Add(stat_grid_sizer, wx.ID_ANY, wx.EXPAND, 20)

        ## =============================== Управление рандомными статами ========================= ##

        # Создаем чекбоксы для каждого стата на который может упасть рандомный стат предмета
        strength_check = wx.CheckBox(self, label="Strength")
        strength_check.SetFont(stat_font)
        dexterity_check = wx.CheckBox(self, label="Dexterity")
        dexterity_check.SetFont(stat_font)
        endurance_check = wx.CheckBox(self, label="Endurance")
        endurance_check.SetFont(stat_font)
        technic_check = wx.CheckBox(self, label="Technic")
        technic_check.SetFont(stat_font)
        speed_check = wx.CheckBox(self, label="Speed")
        speed_check.SetFont(stat_font)

        # Засовываем чекбоксы в грид
        checkbox_sizer = wx.GridSizer(cols=3, hgap=10, vgap=10)
        checkbox_sizer.Add(strength_check)
        checkbox_sizer.Add(dexterity_check)
        checkbox_sizer.Add(endurance_check)
        checkbox_sizer.Add(technic_check)
        checkbox_sizer.Add(speed_check)

        random_label = wx.StaticText(self, label="Random stat distribution")
        random_label.SetFont(label_font)

        # Добавляем все элементы блока рандомных статов в один сайзер
        rand_sizer = wx.BoxSizer(wx.VERTICAL)
        rand_sizer.Add(random_label, wx.ID_ANY, wx.ALIGN_CENTER)
        rand_sizer.Add(checkbox_sizer, wx.ID_ANY, wx.ALIGN_CENTER_HORIZONTAL)


        ## =============================== Кнопки управления =================================

        test_button = wx.Button(self, label="Test")
        self.Bind(wx.EVT_BUTTON, self.show_current_item_stats, test_button)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(test_button, wx.ID_ANY, wx.ALIGN_CENTER)


        ##=============================== Главный сайзер================================
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_sizer.Add(self.top_sizer, wx.ID_ANY, wx.EXPAND, wx.BOTTOM, 20)
        self.main_sizer.Add(self.mod_section, wx.ID_ANY, wx.EXPAND, wx.BOTTOM, 20)
        self.main_sizer.Add(self.stat_sizer, wx.ID_ANY, wx.EXPAND, wx.BOTTOM, 20)
        self.main_sizer.Add(rand_sizer, wx.ID_ANY, wx.EXPAND, wx.BOTTOM, 20)
        self.main_sizer.Add(button_sizer, wx.ID_ANY, wx.EXPAND)

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

    def show_current_item_stats(self, e):
        self.str_amount_txt.SetLabel(f"Strength: {self.current_item.stat_bonuses['Strength']}")
        self.dex_amount_txt.SetLabel(f"Dexterity: {self.current_item.stat_bonuses['Dexterity']}")
        self.end_amount_txt.SetLabel(f"Endurance: {self.current_item.stat_bonuses['Endurance']}")
        self.spd_amount_txt.SetLabel(f"Speed: {self.current_item.stat_bonuses['Speed']}")
        self.tech_amount_txt.SetLabel(f"Technic: {self.current_item.stat_bonuses['Technic']}")
        self.hit_amount_txt.SetLabel(f"Hit chance: {self.current_item.stat_bonuses['HitChance']}")
        self.crit_amount_txt.SetLabel(f"Crit chance: {self.current_item.stat_bonuses['Crit']}")
        self.effic_amount_txt.SetLabel(f"Efficiency: {self.current_item.stat_bonuses['DebuffEfficiency']}")
        self.dodge_amount_txt.SetLabel(f"Efficency: {self.current_item.stat_bonuses['DodgeChance']}")
        self.resphys_amount_txt.SetLabel(f"ResPhys: {self.current_item.stat_bonuses['ResPhys']}")
        self.reschem_amount_txt.SetLabel(f"ResChem: {self.current_item.stat_bonuses['ResChem']}")
        self.restherm_amount_txt.SetLabel(f"ResThern: {self.current_item.stat_bonuses['ResThermo']}")
        self.heal_amount_txt.SetLabel(f"Heal bonus: {self.current_item.stat_bonuses['Heal']}")
        self.power_amount_txt.SetLabel(f"Power: {self.current_item.stat_bonuses['Power']}")

    def update_new_item_stats(self, e):
        temp_mod_list = []
        for mod in self.mod_boxes:
            name = mod.GetValue()
            new_mod = Crafting.CraftMod(name)
            temp_mod_list.append(new_mod)

        temp_item_name = self.item_type.GetValue()
        temp_type = self.item_key_combobox.GetValue()
        temp_rarity = self.item_rarity_value.GetValue()

        new_item = Equipment.EquipmentCommon(temp_type, temp_rarity, name=temp_item_name, mod_list=temp_mod_list)
        self.current_item = new_item
        self.show_current_item_stats(e)













