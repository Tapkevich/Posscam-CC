import wx
import Main
import Manager
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
    def __init__(self, parent, title):
        super(FirstLayer, self).__init__(parent, title=title)
        self.init_ui()
        self.Centre()

    def init_ui(self):

        # Создаем список вещей для дальнейшего использования во вьюхах
        item_storage = Manager.ItemStorage()
        item_storage.load_unique_items()
        item_storage.load_common_items()

        p = wx.Panel(self)
        nb = wx.Notebook(p)

        page_1 = MainMenu(nb)
        page_2 = CharacterList(nb, item_storage)

        # Вкладка со списком предметов, передаем в нее item_storage со списком предметов
        page_3 = ItemList(nb, item_storage)

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
    def __init__(self, parent, item_dict):
        wx.Panel.__init__(self, parent)
        self.item_dict = item_dict
        self.ui_init()

    def ui_init(self):
        pass


class ItemList(wx.Panel):
    def __init__(self, parent, item_storage):
        wx.Panel.__init__(self, parent)
        self.item_storage = item_storage
        self.item_list = wx.ListBox(self, -1)
        self.ui_init()

    def ui_init(self):

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        add_item_button = wx.Button(self, -1, "Add")
        remove_item_button = wx.Button(self, -1, "Remove")
        modify_item_button = wx.Button(self, -1, "Change")

        add_item_button.Bind(wx.EVT_BUTTON, self.add_item)

        for key, item in self.item_storage.item_dict.items():
            self.item_list.Append(key)
        # item_list = wx.ListCtrl(self, -1, name="Item list")
        # item_list.InsertColumn(0, "Item key", width=100)
        # item_list.InsertColumn(1, "Item type", wx.LIST_FORMAT_RIGHT, 100)

        # for key, item in self.item_dict.items():
        #     # index = item_list.InsertStringItem(item_list.GetItemCount()+1, item.key)
        #     # item_list.SetStringItem(index, 1, item.type)
        #     count = item_list.GetItemCount()+1
        #     item_list.InsertItem(count, key)
        some_text = wx.StaticText(self, -1, "ITEM LIBRARY")

        button_sizer.Add(add_item_button, wx.ID_ANY)
        button_sizer.Add(modify_item_button, wx.ID_ANY)
        button_sizer.Add(remove_item_button, wx.ID_ANY)

        main_sizer.Add(some_text, wx.ID_ANY, 0, wx.ALIGN_BOTTOM, 0)
        main_sizer.Add(self.item_list, wx.ID_ANY, wx.EXPAND)
        main_sizer.Add(button_sizer, wx.ID_ANY, wx.EXPAND)

        self.SetSizer(main_sizer)

        # main_sizer.SetSizeHints(item_list)

    def add_item(self, e):
        new_item = self.item_storage.create_item()
        print(new_item.name)
        Manager.ItemStorage.add_item(self.item_storage, new_item)
        self.item_list.Clear()
        for key, item in self.item_storage.item_dict.items():
            self.item_list.Append(key)










