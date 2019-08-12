import BaseStats
import Manager
import Interface
import wx






def main():

    item_storage = Manager.ItemStorage()
    item_storage.load_unique_items()
    item_storage.load_common_items()



    app = wx.App()
    main_menu = Interface.FirstLayer(None, "Combat calc")
    main_menu.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()