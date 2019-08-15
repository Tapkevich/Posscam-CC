import BaseStats
import Manager
import Interface
import wx
import Storage


def main():



    app = wx.App()
    main_menu = Interface.FirstLayer(None)
    main_menu.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()