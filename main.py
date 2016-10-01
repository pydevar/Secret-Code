#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gi
from src.colors.colors import Colors
from src.generator.secret_code import SecretCode

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk


class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Secret Code")

		self.set_default_size(470, 550)
		self.color = Colors()
		self.add(self.fixeds_main())
		self.start_game()

	def fixeds_main(self):
		fixed_main = self.fixed_creator(0, 0, 0)
		fixed_main.put(self.buttons(), 0, 0)
		fixed_main.put(self.color_options(), 10, 50)
		fixed_main.put(self.colors_screen(), 90, 50)
		fixed_main.put(self.hits_screen(), 345, 75)

		return fixed_main

	def color_options(self):
		frame_color_options = self.frame_creator(0, 60, 400)
		fixed_color_options = self.fixed_creator(5, 0, 0)
		self.panel_color_options(fixed_color_options)
		evntbox_color_options = Gtk.EventBox()
		evntbox_color_options.add(fixed_color_options)
		evntbox_color_options.connect("button-press-event", self.select_color)
		frame_color_options.add(evntbox_color_options)
		return frame_color_options

	def colors_screen(self):

		frame_color_screen = self.frame_creator(0, 250, 350)
		fixed_color_screen = self.fixed_creator(10, 10, 10)

		self.image_panel = []
		self.panel_creator_default(self.image_panel, fixed_color_screen)

		evntbox_color_screen = Gtk.EventBox()
		evntbox_color_screen.add(fixed_color_screen)
		evntbox_color_screen.connect("button-press-event", self.deselect_color)

		frame_color_screen.add(evntbox_color_screen)
		return frame_color_screen

	def hits_screen(self):

		frame_hits = self.frame_creator(10, 105, 200)
		fixed_hits = self.fixed_creator(5, 5, 5)

		self.color_hits = []
		self.panel_creator_default(self.color_hits, fixed_hits, 20, 20, 25, 70)

		frame_hits.add(fixed_hits)
		return frame_hits

	def buttons(self):

		fixed_buttons = self.fixed_creator(0, 0, 0)
		button_reset = Gtk.Button("Reset and New Game")

		button_reset.connect("clicked", self.reset_game)

		fixed_buttons.put(button_reset, 100, 10)

		return fixed_buttons

	@staticmethod
	def frame_creator(frame_margin_left, frame_width, frame_height):
		frame = Gtk.Frame()
		frame.set_margin_left(frame_margin_left)
		frame.set_size_request(frame_width, frame_height)

		return frame

	@staticmethod
	def fixed_creator(margin_left, margin_bottom, margin_top):
		fixed = Gtk.Fixed()
		fixed.set_margin_left(margin_left)
		fixed.set_margin_bottom(margin_bottom)
		fixed.set_margin_top(margin_top)

		return fixed

	def panel_creator_default(self, to_list, fixed, width=50, height=50, jump_one=60, jump_two=80):

		step = 0
		step2 = 0
		for z in range(0, 6):
			for i in range(0, 4):
				color_image = Gtk.Image()
				color_hit_pixbuff = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.color.get_color(0), width, height, False)
				color_image.set_from_pixbuf(color_hit_pixbuff)
				to_list.append([color_image, 0 + step, step2])
				step += jump_one
			step2 += jump_two
			step = 0

		for color_image in to_list:
			fixed.put(color_image[0], color_image[1], color_image[2])

	def panel_color_options(self, fixed):
		step = 0
		for key, imagePath in self.color.get_dictionary():
			if not key == 0:
				colorOption = Gtk.Image()
				colorOption.set_from_file(imagePath)
				fixed.put(colorOption, 0, step)
				step += 60

	def select_color(self, eventbox, event):
		post_y = int(event.y // 60) + 1

		if event.type == Gdk.EventType.BUTTON_PRESS:
			if self.turn<24:
				self.image_panel[self.turn][0].set_from_file(self.color.get_color(post_y))
				self.turn += 1

				if self.turn<=4:
					self.guesses[0].append(post_y-1)
					self.guess_hints()
				if  4< self.turn <=8:
					self.guesses[1].append(post_y-1)
					self.guess_hints()
				if 8<self.turn <= 12:
					self.guesses[2].append(post_y-1)
					self.guess_hints()
				if 12<self.turn <= 16:
					self.guesses[3].append(post_y-1)
					self.guess_hints()
				if  16<self.turn <= 20:
					self.guesses[4].append(post_y-1)
					self.guess_hints()
				if 20<self.turn <= 24:
					self.guesses[5].append(post_y-1)
					self.guess_hints()

	def guess_hints(self):
		print "este es",self.secret_code.get_secret_code()
		self.code_guess_turn=self.turn//4-1

		if self.check_turn_hints():
			self.secret_code.compare_codes(self.guesses[self.code_guess_turn])
			print self.guesses[self.code_guess_turn]
			print self.secret_code.get_hints()
			self.recolour_hits(self.code_guess_turn)

	def check_turn_hints(self):
		return self.turn !=0 and self.turn % 4==0

	def recolour_hits(self, turn):

		for i in range(0 + (turn*4),4 + (turn*4),1):
			pixbuf_hits = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.color.get_color(self.secret_code.get_hints()[i%4]), 20, 20, False)
			self.color_hits[i][0].set_from_pixbuf(pixbuf_hits)

	def reset_hits(self):
		for hit in self.color_hits:
			start_pixbuff=GdkPixbuf.Pixbuf.new_from_file_at_scale(self.color.get_color(0), 20, 20, False)
			hit[0].set_from_pixbuf(start_pixbuff)

	def reset_game(self, button):
		for image in self.image_panel:
			image[0].set_from_file(self.color.get_color(0))

		self.start_game()
		self.reset_hits()

	def start_game(self):
		self.turn = 0
		self.guesses = [[], [], [], [], [], []]
		self.secret_code = SecretCode()


	def deselect_color(self, eventbox, event):
		if event.type == Gdk.EventType.BUTTON_PRESS:
			if self.turn == 24:
				pass
			elif self.turn ==18:
				pass
			elif self.turn == 12:
				pass
			elif self.turn == 8:
				pass
			elif self.turn == 4:
				pass
			elif self.turn > 0:
					self.guesses[self.turn // 4].pop()
					self.turn -= 1
					self.image_panel[self.turn][0].set_from_file(self.color.get_color(0))




main = MainWindow()
main.show_all()
main.connect("delete-event", Gtk.main_quit)
Gtk.main()
