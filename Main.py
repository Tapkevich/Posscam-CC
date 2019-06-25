import BaseStats
import Manager
import wx

# monster_storage = Manager.MonsterStorage()
# monster_storage.get_monsters(Manager.MonsterGenerator().create_monsters(BaseStats.monster_keys,
#                                                                         BaseStats.monster_base_param))
# for m in monster_storage.monster_list:
#     temp_list = m.get_monster_skills()
#     for s in temp_list:
#         if len(s.key) == 0:
#             continue
#         else:
#             print(s.key)

# print(monster_storage.monster_list[1].get_monster_skills())

APP_EXIT = 1

class Example(wx.Frame):
    def __init__(self,*args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        viewMenu = wx.Menu()

        self.shst = viewMenu.Append(wx.ID_ANY, 'Show statusbar', 'Show statusbar', kind = wx.ITEM_CHECK)
        self.shtl = viewMenu.Append(wx.ID_ANY, 'Show toolbar', 'Show Toolbar', kind = wx.ITEM_CHECK)

        viewMenu.Check(self.shst.GetId(), True)
        viewMenu.Check(self.shtl.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)

        menubar.Append(viewMenu, '&View')
        self.SetMenuBar(menubar)

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddTool(1,'', wx.Bitmap('1.png'))
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

        self.SetSize((450, 350))
        self.SetTitle('Check menu item')
        self.Centre()

    def ToggleStatusBar(self, e):
        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, e):
        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()



def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()