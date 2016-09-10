#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Secret Code")

        self.turn = 0
        self.set_default_size(450, 550)

        self.colors = {0: "imgs/default.png",
                       1: "imgs/blue.png",
                       2: "imgs/green.png",
                       3: "imgs/red.png",
                       4: "imgs/orange.png",
                       5: "imgs/pink.png",
                       6: "imgs/purple.png",
                       7: "imgs/white.png",
                       8: "imgs/yellow.png"}

        fixed = Gtk.Fixed()
        fixed.put(self.botones(), 0, 0)
        fixed.put(self.temp(), 10, 50)
        fixed.put(self.codigoPanel(), 100, 50)
        fixed.put(self.aciertos(), 345, 75)
        self.add(fixed)

    def temp(self):
        frame = Gtk.Frame()
        fixed = Gtk.Fixed()

        blue = Gtk.Image()
        pixbufblue = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.colors.get(1), 50, 50, False)
        blue.set_from_pixbuf(pixbufblue)

        green = Gtk.Image()
        pixbufgreen = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.colors.get(2), 50, 50, False)
        green.set_from_pixbuf(pixbufgreen)

        red = Gtk.Image()
        pixbufred = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.colors.get(3), 50, 50, False)
        red.set_from_pixbuf(pixbufred)

        orange = Gtk.Image()
        pixbufblue = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.colors.get(4), 50, 50, False)
        orange.set_from_pixbuf(pixbufblue)

        pink = Gtk.Image()
        pixbufblue = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.colors.get(5), 50, 50, False)
        pink.set_from_pixbuf(pixbufblue)

        purple = Gtk.Image()
        pixbufblue = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.colors.get(6), 50, 50, False)
        purple.set_from_pixbuf(pixbufblue)

        white = Gtk.Image()
        pixbufblue = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.colors.get(7), 50, 50, False)
        white.set_from_pixbuf(pixbufblue)

        yellow = Gtk.Image()
        pixbufblue = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.colors.get(8), 50, 50, False)
        yellow.set_from_pixbuf(pixbufblue)

        fixed.put(blue, 0, 0)
        fixed.put(green, 0, 60)
        fixed.put(red, 0, 120)
        fixed.put(orange, 0, 180)
        fixed.put(pink, 0, 240)
        fixed.put(purple, 0, 300)
        fixed.put(white, 0, 360)
        fixed.put(yellow, 0, 420)

        eventBox = Gtk.EventBox()
        eventBox.add(fixed)
        eventBox.connect("button-press-event", self.select_color)

        frame.add(eventBox)
        return frame

    def codigoPanel(self):

        frame = Gtk.Frame()
        fixed = Gtk.Fixed()

        self.imagePanel = []

        step = 0
        step2 = 0
        for z in range(0, 6):
            for i in range(0, 4):
                self.tempImage = Gtk.Image()
                pixbufgreen = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.colors.get(0), 50, 50, False)
                self.tempImage.set_from_pixbuf(pixbufgreen)
                self.imagePanel.append([self.tempImage, 0 + step, step2])
                step += 60
            step2 += 80
            step = 0

        for image in self.imagePanel:
            fixed.put(image[0], image[1], image[2])

        frame.add(fixed)
        return frame

    def aciertos(self):
        frame = Gtk.Frame()
        fixed = Gtk.Fixed()

        step = 0
        step2 = 0
        for z in range(0, 6):

            for i in range(0, 4):
                temp = Gtk.Image()
                pixbufgreen = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.colors.get(0), 20, 20, False)
                temp.set_from_pixbuf(pixbufgreen)
                fixed.put(temp, 0 + step, step2)
                step += 25
            step2 += 70
            step = 0

        frame.add(fixed)
        return frame

    def botones(self):

        fixed = Gtk.Fixed()
        buttonStart = Gtk.Button("Start")
        buttonReset = Gtk.Button("Reset")

        buttonReset.connect("clicked", self.reset_game)

        fixed.put(buttonStart, 10, 10)
        fixed.put(buttonReset, 100, 10)

        return fixed

    def select_color(self, eventbox, event):

        posy = int(event.y // 60) + 1
        self.imagePanel[self.turn][0].set_from_file(self.colors.get(posy))
        self.turn += 1

        print self.turn
        print (posy)

    def reset_game(self, button):
        for image in self.imagePanel:
            image[0].set_from_file(self.colors.get(0))
        self.turn = 0


mainwindow = MainWindow()
mainwindow.show_all()
mainwindow.connect("delete-event", Gtk.main_quit)
Gtk.main()
