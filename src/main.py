#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018 Purism SPC
# SPDX-License-Identifier: GPL-3.0+
# Author: David Boddie <david.boddie@puri.sm>

import sys
import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, Vte
import os


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='asgardius.page.aoilauncher')
        GLib.set_application_name('Aoi Game Launcher')
        GLib.set_prgname('asgardius.page.aoilauncher')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self)
        window.set_icon_name('asgardius.page.aoilauncher')

        hbox = Gtk.VBox(spacing=6)
        window.add(hbox)

        label = Gtk.Label()
        label.set_markup('<span font="12">Do you want a healer?\nNow you have one</span>')
        hbox.pack_start(label, True, True, 0)

        button = Gtk.Button.new_with_label("Install / Update")
        button.connect("clicked", self.on_install_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Play")
        button.connect("clicked", self.on_play_clicked)
        hbox.pack_start(button, True, True, 0)
        #window.add(label)
        window.show_all()

    def on_install_clicked(self, button):
        home = os.path.expanduser("~")
        terminal     = Vte.Terminal()
        terminal.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            None,
            ['/bin/bash', '-c', ' wget https://lily.asgardius.company/midoridlx64 -O '+home+'/.r3game && chmod +x '+home+'/.asgardius.page.virtualxrpg && echo \"Game Installed\"'],
            None,
            GLib.SpawnFlags.DEFAULT,
        )

        win = Gtk.Window()
        win.connect('delete-event', Gtk.main_quit)
        win.add(terminal)
        win.show_all()

    def on_play_clicked(self, button):
        home = os.path.expanduser("~")
        subprocess.run([home+'/.asgardius.page.virtualxrpg'])


if __name__ == "__main__":

    app = Application()
    result = app.run(sys.argv)
    sys.exit(result)
