import wx
APP_EXIT = 1

class MiscFunctions():
    @staticmethod
    def scale_bitmap_image(bitmap, width, height):
        image = bitmap.ConvertToImage()
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result


class MainMenu(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "Some shity tet 1", (20, 20))
        self.ui_stuff()


    def ui_stuff (self):

        sd = wx.StaticText(self, -1, "2nd line", (20, 40))




class CharacterList(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "Some shity tet 2", (40, 40))
        self.ui_init()

    def ui_init(self):
        pass





class FirstLayer(wx.Frame):
    def __init__(self, parent, title):
        super(FirstLayer, self).__init__(parent, title=title)
        self.InitUi()
        self.Centre()


    def InitUi(self):

        main_menu_bitmap = wx.Bitmap('img/main_menu.png')
        main_menu_bitmap = MiscFunctions.scale_bitmap_image(main_menu_bitmap, 30, 30)
        character_list_bitmap = wx.Bitmap('img/mercenary_list.png')
        character_list_bitmap = MiscFunctions.scale_bitmap_image(character_list_bitmap, 30, 30)
        equipment_list_bitmap = wx.Bitmap('img/equipment_list.png')
        equipment_list_bitmap = MiscFunctions.scale_bitmap_image(equipment_list_bitmap, 30, 30)
        combat_calc_bitmap = wx.Bitmap('img/combat.png')
        combat_calc_bitmap = MiscFunctions.scale_bitmap_image(combat_calc_bitmap, 30, 30)
        economy_calc_bitmap = wx.Bitmap('img/economy_calc.png')
        economy_calc_bitmap = MiscFunctions.scale_bitmap_image(economy_calc_bitmap, 30, 30)

        # self.toolbar = self.CreateToolBar()
        # self.toolbar.AddTool(1, 'Main menu', main_menu_bitmap)
        # self.toolbar.AddSeparator()
        # self.toolbar.AddTool(2, 'Text', character_list_bitmap)
        # self.toolbar.AddSeparator()
        # self.toolbar.AddTool(3, "Equipment_list", equipment_list_bitmap)
        # self.toolbar.AddSeparator()
        # self.toolbar.AddTool(4, "Combat_calc", combat_calc_bitmap)
        # self.toolbar.AddSeparator()
        # self.toolbar.AddTool(4, "Economy calc", economy_calc_bitmap)
        # self.toolbar.AddSeparator()
        # self.toolbar.Realize()
        p = wx.Panel(self)
        nb = wx.Notebook(p)

        page_1 = MainMenu(nb)
        page_2 = CharacterList(nb)

        nb.AddPage(page_1, "Page 1")
        nb.AddPage(page_2, "Page 2")

        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)

        self.SetSize((800, 800))
        self.SetTitle('Main menu')
        self.SetBackgroundColour("GRAY")
