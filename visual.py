#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk


class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Secret Code")

		self.turn = 0
		self.set_default_size(470, 550)

		self.colors = {0: "imgs/default.png",
					   1: "imgs/blue.png",
					   2: "imgs/green.png",
					   3: "imgs/red.png",
					   4: "imgs/orange.png",
					   5: "imgs/pink.png",
					   6: "imgs/purple.png",
					   7: "imgs/white.png",
					   8: "imgs/yellow.png"}

		fixedMain = self.fixed_creator(0, 0, 0)
		fixedMain.put(self.buttons(), 0, 0)
		fixedMain.put(self.colorOptions(), 10, 50)
		fixedMain.put(self.colorsScreen(), 90, 50)
		fixedMain.put(self.hits(), 345, 75)
		self.add(fixedMain)

	def colorOptions(self):
		frameColorOptions = self.frame_creator(0, 60, 400)
		fixedColorOptions = self.fixed_creator(5, 0, 0)

		self.panel_color_options(fixedColorOptions)

		eventBoxColorOptions = Gtk.EventBox()
		eventBoxColorOptions.add(fixedColorOptions)
		eventBoxColorOptions.connect("button-press-event", self.select_color)

		frameColorOptions.add(eventBoxColorOptions)
		return frameColorOptions

	def colorsScreen(self):

		frameColorScreen = self.frame_creator(0, 250, 350)
		fixedColorScreen = self.fixed_creator(10, 10, 10)

		self.imagePanel = []
		self.panel_creator_default(self.imagePanel, fixedColorScreen)

		eventBoxColorScreen = Gtk.EventBox()
		eventBoxColorScreen.add(fixedColorScreen)
		eventBoxColorScreen.connect("button-press-event", self.deselect_color)

		frameColorScreen.add(eventBoxColorScreen)
		return frameColorScreen

	def hits(self):

		frameHits = self.frame_creator(10, 105, 200)
		fixedHits = self.fixed_creator(5, 5, 5)

		self.colorHits = []
		self.panel_creator_default(self.colorHits, fixedHits, 20, 20, 25, 70)

		frameHits.add(fixedHits)
		return frameHits

	def buttons(self):

		fixedButtons = self.fixed_creator(0, 0, 0)
		# buttonStart = Gtk.Button("Compare")
		buttonReset = Gtk.Button("Reset and New Game")

		buttonReset.connect("clicked", self.reset_game)

		# fixedButtons.put(buttonStart, 10, 10)
		fixedButtons.put(buttonReset, 100, 10)

		return fixedButtons

	def frame_creator(self, frameMarginLeft, frameWidth, frameHeight):
		frame = Gtk.Frame()
		frame.set_margin_left(frameMarginLeft)
		frame.set_size_request(frameWidth, frameHeight)

		return frame

	def fixed_creator(self, marginLeft, marginBottom, marginTop):
		fixed = Gtk.Fixed()
		fixed.set_margin_left(marginLeft)
		fixed.set_margin_bottom(marginBottom)
		fixed.set_margin_top(marginTop)

		return fixed

	def panel_creator_default(self, toList, fixed, width=50, height=50, jump_one=60, jump_two=80):

		step = 0
		step2 = 0
		for z in range(0, 6):
			for i in range(0, 4):
				colorImage = Gtk.Image()
				colorHitPixbuff = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.colors.get(0), width, height, False)
				colorImage.set_from_pixbuf(colorHitPixbuff)
				toList.append([colorImage, 0 + step, step2])
				step += jump_one
			step2 += jump_two
			step = 0

		for colorImage in toList:
			fixed.put(colorImage[0], colorImage[1], colorImage[2])

	def panel_color_options(self, fixed):
		step = 0
		for key, imagePath in self.colors.items():
			if not key == 0:
				colorOption = Gtk.Image()
				colorOption.set_from_file(imagePath)
				fixed.put(colorOption, 0, step)
				step += 60

	def select_color(self, eventbox, event):

		posy = int(event.y // 60) + 1
		self.imagePanel[self.turn][0].set_from_file(self.colors.get(posy))
		self.turn += 1

	def reset_game(self, button):
		for image in self.imagePanel:
			image[0].set_from_file(self.colors.get(0))
		self.turn = 0

	def deselect_color(self, eventbox, event):
		if self.turn > 0:
			self.turn -= 1
			self.imagePanel[self.turn][0].set_from_file(self.colors.get(0))


mainwindow = MainWindow()
mainwindow.show_all()
mainwindow.connect("delete-event", Gtk.main_quit)
Gtk.main()
