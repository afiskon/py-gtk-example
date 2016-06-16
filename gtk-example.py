#!/usr/bin/env python3

# gtk-example.py
# (c) Aleksander Alekseev 2016
# http://eax.me/

import signal
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import AppIndicator3 as AI
from gi.repository import Notify


APPID = "GTK Test"
# could be PNG, SVG or even Gtk.STOCK_INFO as well
ICON = '/usr/share/pixmaps/python3.xpm'


class Handler:

    def __init__(self):
        self.window_is_hidden = False

    def onShowButtonClicked(self, button):
        msg = "Clicked: " + entry.get_text()
        dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.OK, msg)
        dialog.run()
        dialog.destroy()

    def onNotify(self, *args):
        Notify.Notification.new("Notification", "Hello!", ICON).show()

    def onShowOrHide(self, *args):
        if self.window_is_hidden:
            window.show()
        else:
            window.hide()

        self.window_is_hidden = not self.window_is_hidden

    def onQuit(self, *args):
        Notify.uninit()
        Gtk.main_quit()

# Handle pressing Ctr+C properly, ignored by default
signal.signal(signal.SIGINT, signal.SIG_DFL)

builder = Gtk.Builder()
builder.add_from_file('gtk-example.glade')
builder.connect_signals(Handler())

window = builder.get_object('window1')
window.set_icon_from_file(ICON)
window.show_all()

entry = builder.get_object('entry1')
menu = builder.get_object('menu1')

ai = AI.Indicator.new(APPID, ICON, AI.IndicatorCategory.SYSTEM_SERVICES)
ai.set_status(AI.IndicatorStatus.ACTIVE)
ai.set_menu(menu)  # NB: menu is required!

Notify.init(APPID)
Gtk.main()
