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

        ##============================= Шрифты ===============================##

        label_font = wx.Font(16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        sublabel_font = wx.Font(12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        stat_font = wx.Font(16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)

        ##================================ Верхний блок ==========================



    # def update_new_item_stats(self, e):
    #     temp_mod_list = []
    #     for mod in self.mod_boxes:
    #         name = mod.GetValue()
    #         new_mod = Crafting.CraftMod(name)
    #         temp_mod_list.append(new_mod)
    #
    #     temp_item_name = self.current_item.name
    #     temp_type = self.item_key_combobox.GetValue()
    #     temp_rarity = self.item_rarity_value.GetValue()
    #
    #     new_item = Equipment.EquipmentCommon(temp_type, temp_rarity, name=temp_item_name, mod_list=temp_mod_list)
    #     self.current_item = new_item
    #     self.show_current_item_stats(e)













