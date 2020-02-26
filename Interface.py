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
        self.Size = wx.Size(500, 600)

        self.current_item = self.find_current_item(item)
        common_item_types = Storage.ItemStorage.get_common_item_keys()

        self.Bind(wx.EVT_SHOW, self.show_current_item_stats)

        mod_list = []
        mod_list.append("None")
        for key, value in Storage.item_storage.mod_dict.items():
            mod_list.append(key)

        # Главная панель
        main_panel = wx.Panel(self)
        main_panel.SetBackgroundColour('#484f49')

        ##============================= Шрифты ===============================##

        label_font = wx.Font(16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        sublabel_font = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        stat_font = wx.Font(16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)

        # ============================= Заголовок ======================================
        label_panel = wx.Panel(main_panel, pos=(0, 0))
        label_panel.SetSize(500, 30)
        label_panel.SetBackgroundColour('#46f057')
        label_text = wx.StaticText(label_panel, label="Item information")
        label_text.SetFont(label_font)
        label_text.SetForegroundColour('#6b756c')
        label_text.SetPosition((170, 5))


        ##================================ Верхний блок ==========================

        top_panel = wx.Panel(main_panel, pos=(10, 30))
        top_panel.SetSize(460, 70)
        top_panel.SetBackgroundColour('#1271e6')
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Создаем коробку с именем предмета
        item_name_sizer = wx.BoxSizer(wx.VERTICAL)

        item_name_label = wx.StaticText(top_panel, label="Current item name")
        item_name_label.SetFont(sublabel_font)
        self.item_name_ctrl = wx.TextCtrl(top_panel, value=self.current_item.name)

        item_name_sizer.AddSpacer(7)
        item_name_sizer.Add(item_name_label, 0, wx.ALIGN_CENTER_HORIZONTAL)
        item_name_sizer.AddSpacer(5)
        item_name_sizer.Add(self.item_name_ctrl, wx.EXPAND)
        top_sizer.Add(item_name_sizer, 0, wx.LEFT | wx.RIGHT, border=5)

        # Создаем коробку с типом предмета
        item_key_sizer = wx.BoxSizer(wx.VERTICAL)

        item_key_label = wx.StaticText(top_panel, label="Item key")
        item_key_label.SetFont(sublabel_font)
        self.item_key_cbox = wx.ComboBox(top_panel, value=self.current_item.key, choices=common_item_types)

        item_key_sizer.AddSpacer(7)
        item_key_sizer.Add(item_key_label, 0, wx.ALIGN_CENTER_HORIZONTAL)
        item_key_sizer.AddSpacer(5)
        item_key_sizer.Add(self.item_key_cbox, wx.EXPAND)
        top_sizer.Add(item_key_sizer, 0, wx.LEFT | wx.RIGHT, border=5)

        # Создаем коробку с редкостью предмета
        item_rarity_sizer = wx.BoxSizer(wx.VERTICAL)

        item_rarity_label = wx.StaticText(top_panel, label="Item rarity")
        item_rarity_label.SetFont(sublabel_font)
        self.item_rarity_cbox = wx.ComboBox(top_panel, value=self.current_item.rarity.key, choices=BaseStats.RARITY_LIST)

        item_rarity_sizer.AddSpacer(7)
        item_rarity_sizer.Add(item_rarity_label, 0, wx.ALIGN_CENTER_HORIZONTAL)
        item_rarity_sizer.AddSpacer(5)
        item_rarity_sizer.Add(self.item_rarity_cbox, wx.EXPAND)
        top_sizer.Add(item_rarity_sizer, 0, wx.LEFT | wx.RIGHT, border=5)

        top_panel.SetSizer(top_sizer)
        top_panel.Layout()




        # =============================== Настройка модов ==================================

        mod_panel = wx.Panel(main_panel, pos=(10, 100))
        mod_panel.SetSize(460, 140)
        mod_panel.SetBackgroundColour('#6b756c')
        mod_sizer = wx.BoxSizer(wx.VERTICAL)
        mod_intermediate_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Коробка с первым модом
        first_mod_sizer = wx.BoxSizer(wx.VERTICAL)

        first_mod_label = wx.StaticText(mod_panel, label="First mod")
        first_mod_label.SetFont(sublabel_font)
        first_mod_cbox = wx.ComboBox(mod_panel, value=self.current_item.mod_list[0].key, choices=mod_list)

        # first_mod_sizer.AddSpacer(7)
        first_mod_sizer.Add(first_mod_label, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
        first_mod_sizer.AddSpacer(5)
        first_mod_sizer.Add(first_mod_cbox, flag=wx.EXPAND)
        mod_intermediate_sizer.Add(first_mod_sizer, 1, wx.LEFT | wx.RIGHT, border=5)

        # Коробка со вторым модом
        second_mod_sizer = wx.BoxSizer(wx.VERTICAL)

        second_mod_label = wx.StaticText(mod_panel, label='Second mod')
        second_mod_label.SetFont(sublabel_font)
        second_mod_cbox = wx.ComboBox(mod_panel, value=self.current_item.mod_list[1].key,
                                      choices=mod_list)

        # second_mod_sizer.AddSpacer(7)
        second_mod_sizer.Add(second_mod_label, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
        second_mod_sizer.AddSpacer(5)
        second_mod_sizer.Add(second_mod_cbox, 0)
        mod_intermediate_sizer.Add(second_mod_sizer, 1, flag=wx.LEFT | wx.RIGHT, border=5)

        # Коробка с третьим модом

        third_mod_sizer = wx.BoxSizer(wx.VERTICAL)

        third_mod_label = wx.StaticText(mod_panel, label="Third mod")
        third_mod_label.SetFont(sublabel_font)
        third_mod_cbox = wx.ComboBox(mod_panel, value=self.current_item.mod_list[2].key,
                                     choices=mod_list)
        third_mod_cbox.SetFont(sublabel_font)

        # third_mod_sizer.AddSpacer(7)
        third_mod_sizer.Add(third_mod_label, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
        third_mod_sizer.AddSpacer(5)
        third_mod_sizer.Add(third_mod_cbox, 0, wx.EXPAND)
        

        # Коробка для всей мод панели + ее заголовок

        mod_panel_label = wx.StaticText(mod_panel, label="Mods")
        mod_panel_label.SetFont(label_font)

        mod_sizer.AddSpacer(5)
        mod_sizer.Add(mod_panel_label, 0, wx.ALIGN_CENTER_HORIZONTAL)
        # mod_sizer.AddSpacer(5)
        mod_sizer.Add(mod_intermediate_sizer, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
        mod_sizer.AddSpacer(5)
        mod_sizer.Add(third_mod_sizer, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)

        mod_panel.SetSizer(mod_sizer)
        mod_panel.Layout()




        # ========================= Параметры предмета ===================================

        atr_panel = wx.Panel(main_panel, pos=(10, 240))
        atr_panel.SetSize(460, 200)
        atr_panel.SetBackgroundColour('#9f9ca6')

        # Основной сайзер с лабелкой

        atr_main_sizer = wx.BoxSizer(wx.VERTICAL)
        atr_panel_label = wx.StaticText(atr_panel, label="Item stats")
        atr_panel_label.SetFont(label_font)


        # Строки для всех возможных параметров снаряжения

        self.str_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.str_amount_txt.SetFont(stat_font)
        self.dex_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.dex_amount_txt.SetFont(stat_font)
        self.end_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.end_amount_txt.SetFont(stat_font)
        self.spd_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.spd_amount_txt.SetFont(stat_font)
        self.tech_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.tech_amount_txt.SetFont(stat_font)
        self.hit_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.hit_amount_txt.SetFont(stat_font)
        self.crit_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.crit_amount_txt.SetFont(stat_font)
        self.effic_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.effic_amount_txt.SetFont(stat_font)
        self.dodge_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.dodge_amount_txt.SetFont(stat_font)
        self.resphys_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.resphys_amount_txt.SetFont(stat_font)
        self.reschem_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.reschem_amount_txt.SetFont(stat_font)
        self.restherm_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.restherm_amount_txt.SetFont(stat_font)
        self.heal_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.heal_amount_txt.SetFont(stat_font)
        self.power_amount_txt = wx.StaticText(atr_panel, label="Didn't get stat")
        self.power_amount_txt.SetFont(stat_font)

        # Грид сайзер для статов

        atr_grid_sizer = wx.GridSizer(cols=3, vgap=10, hgap=20)
        atr_grid_sizer.Add(self.str_amount_txt)
        atr_grid_sizer.Add(self.dex_amount_txt)
        atr_grid_sizer.Add(self.end_amount_txt)
        atr_grid_sizer.Add(self.spd_amount_txt)
        atr_grid_sizer.Add(self.tech_amount_txt)
        atr_grid_sizer.Add(self.hit_amount_txt)
        atr_grid_sizer.Add(self.crit_amount_txt)
        atr_grid_sizer.Add(self.effic_amount_txt)
        atr_grid_sizer.Add(self.dodge_amount_txt)
        atr_grid_sizer.Add(self.resphys_amount_txt)
        atr_grid_sizer.Add(self.reschem_amount_txt)
        atr_grid_sizer.Add(self.restherm_amount_txt)
        atr_grid_sizer.Add(self.heal_amount_txt)
        atr_grid_sizer.Add(self.power_amount_txt)

        # Добавляем все в основной сайзер

        atr_main_sizer.Add(atr_panel_label, 0, wx.ALIGN_CENTER_HORIZONTAL)
        atr_main_sizer.AddSpacer(10)
        atr_main_sizer.Add(atr_grid_sizer, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
        atr_panel.SetSizer(atr_main_sizer)
        atr_panel.Layout()

        #==================================== Эвенты ============================================

        # Эвенты вкладки с модами
        mod_boxes = (first_mod_cbox, second_mod_cbox, third_mod_cbox)
        first_mod_cbox.Bind(wx.EVT_COMBOBOX, lambda e, boxes=mod_boxes:
                                                    self.update_new_item_stats(e, boxes=boxes))
        second_mod_cbox.Bind(wx.EVT_COMBOBOX, lambda e, boxes=mod_boxes:
                                                    self.update_new_item_stats(e, boxes=boxes))
        third_mod_cbox.Bind(wx.EVT_COMBOBOX, lambda e, boxes=mod_boxes:
                                                    self.update_new_item_stats(e, boxes=boxes))
        # Эвенты топ области
        self.item_name_ctrl.Bind(wx.EVT_TEXT, lambda e, boxes=mod_boxes:
                                                    self.update_new_item_stats(e, boxes=boxes))
        self.item_key_cbox.Bind(wx.EVT_COMBOBOX, lambda e, boxes=mod_boxes:
                                                    self.update_new_item_stats(e, boxes=boxes))
        self.item_rarity_cbox.Bind(wx.EVT_COMBOBOX, lambda e, boxes=mod_boxes:
                                                    self.update_new_item_stats(e, boxes=boxes))

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

    def update_new_item_stats(self, e, boxes):
        temp_mod_list = []
        for mod in boxes:
            mod_key = mod.GetValue()
            new_mod = Crafting.CraftMod(mod_key)
            temp_mod_list.append(new_mod)


        temp_item_name = self.item_name_ctrl.GetValue()
        temp_type = self.item_key_cbox.GetValue()
        temp_rarity = self.item_rarity_cbox.GetValue()

        new_item = Equipment.EquipmentCommon(temp_type, temp_rarity, name=temp_item_name, mod_list=temp_mod_list)
        self.current_item = new_item
        self.show_current_item_stats(e)













