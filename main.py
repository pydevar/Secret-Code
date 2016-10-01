#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
from src.colors.colors import Colors
from src.generator.secret_code import SecretCode


class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Secret Code")
		self.set_default_size(450, 825)
		self.set_position(Gtk.WindowPosition.CENTER)
		self.color = Colors()
		self.toggle_value = False
		self.start_game()
		self.add(self.fixeds_main())

	def fixeds_main(self):
		fixed_main = self.fixed_creator(0, 0, 0)
		fixed_main.put(self.buttons(), 0, 0)
		fixed_main.put(self.color_options(), 10, 60)
		fixed_main.put(self.colors_screen(), 90, 60)
		fixed_main.put(self.hits_screen(), 330, 75)
		fixed_main.put(self.toggle_screen(), 0, 10)

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

		frame_color_screen = self.frame_creator(0, 235, 350)
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
		self.panel_creator_default(self.color_hits, fixed_hits, 20, 20, 24, 75)

		frame_hits.add(fixed_hits)
		return frame_hits

	def toggle_screen(self):
		frame_toggle = self.frame_creator(260, 20, 0)
		fixed_toggle = self.fixed_creator(0, 0, 0)

		self.toggle_hits = []
		self.color_toggle_screen(self.toggle_hits, fixed_toggle)
		frame_toggle.add(fixed_toggle)

		return frame_toggle

	def color_toggle_screen(self, toggle_list, fixed):
		step = 0
		for i in range(0, 4, 1):
			image = Gtk.Image()
			image.set_from_pixbuf(self.get_secret_color(i))
			toggle_list.append([image, 0 + step, 0])
			step += 40
		self.pixbuff_control_toggle()

		for secret_code in toggle_list:
			fixed.put(secret_code[0], secret_code[1], secret_code[2])

	def pixbuff_control_toggle(self, show=False):
		pixbuf_default = GdkPixbuf.Pixbuf.new_from_file_at_scale(
			self.color.get_color(0), 35, 35, False)
		if show:
			for secret_image in range(0, 4, 1):
				self.toggle_hits[secret_image][0].set_from_pixbuf(self.get_secret_color(secret_image))
		else:
			for toggle_hit in self.toggle_hits:
				toggle_hit[0].set_from_pixbuf(pixbuf_default)

	def get_secret_color(self, value):
		pixbuf_secret_code = GdkPixbuf.Pixbuf.new_from_file_at_scale(
			self.color.get_color(self.secret_code.get_secret_code()[value] + 1), 35, 35, False)
		return pixbuf_secret_code

	def buttons(self):

		fixed_buttons = self.fixed_creator(0, 0, 0)
		button_reset = Gtk.Button("Reset and New Game")
		button_reset.connect("clicked", self.reset_game)
		button_toggle = Gtk.Button("Toggle")
		button_toggle.connect("clicked", self.toggle)

		fixed_buttons.put(button_reset, 10, 10)
		fixed_buttons.put(button_toggle, 175, 10)

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

	def panel_creator_default(self, to_list, fixed, width=50, height=50, jump_one=55, jump_two=75):

		step = 0
		step2 = 0
		for z in range(0, 10):
			for i in range(0, 4):
				color_image = Gtk.Image()
				color_hit_pixbuff = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.color.get_color(0), width, height,
																			False)
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
			if self.turn < 40:
				self.image_panel[self.turn][0].set_from_file(self.color.get_color(post_y))
				self.turn += 1

				if self.turn <= 4:
					self.guesses[0].append(post_y - 1)
					self.guess_hints()
				if 4 < self.turn <= 8:
					self.guesses[1].append(post_y - 1)
					self.guess_hints()
				if 8 < self.turn <= 12:
					self.guesses[2].append(post_y - 1)
					self.guess_hints()
				if 12 < self.turn <= 16:
					self.guesses[3].append(post_y - 1)
					self.guess_hints()
				if 16 < self.turn <= 20:
					self.guesses[4].append(post_y - 1)
					self.guess_hints()
				if 20 < self.turn <= 24:
					self.guesses[5].append(post_y - 1)
					self.guess_hints()
				if 24 < self.turn <= 28:
					self.guesses[6].append(post_y - 1)
					self.guess_hints()
				if 28 < self.turn <= 32:
					self.guesses[7].append(post_y - 1)
					self.guess_hints()
				if 32 < self.turn <= 36:
					self.guesses[8].append(post_y - 1)
					self.guess_hints()
				if 36 < self.turn <= 40:
					self.guesses[9].append(post_y - 1)
					self.guess_hints()

	def guess_hints(self):

		self.code_guess_turn = self.turn // 4 - 1

		if self.check_turn_hints():
			self.secret_code.compare_codes(self.guesses[self.code_guess_turn])
			self.recolour_hits(self.code_guess_turn)

	def check_turn_hints(self):
		return self.turn != 0 and self.turn % 4 == 0

	def recolour_hits(self, turn):

		for i in range(0 + (turn * 4), 4 + (turn * 4), 1):
			pixbuf_hits = GdkPixbuf.Pixbuf.new_from_file_at_scale(
				self.color.get_color(self.secret_code.get_hints()[i % 4]), 20, 20, False)
			self.color_hits[i][0].set_from_pixbuf(pixbuf_hits)

	def reset_hits(self):
		for hit in self.color_hits:
			start_pixbuff = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.color.get_color(0), 20, 20, False)
			hit[0].set_from_pixbuf(start_pixbuff)

	def reset_game(self, button):
		for image in self.image_panel:
			image[0].set_from_file(self.color.get_color(0))

		self.start_game()
		self.reset_hits()
		self.pixbuff_control_toggle()

	def toggle(self, button):
		if self.toggle_value:
			self.pixbuff_control_toggle(False)
			self.toggle_value = False
		else:
			self.pixbuff_control_toggle(True)
			self.toggle_value = True

	def start_game(self):
		self.turn = 0
		self.guesses = [[], [], [], [], [], [], [], [], [], []]
		self.toggle_value = False
		self.secret_code = SecretCode()

	def deselect_color(self, eventbox, event):
		if event.type == Gdk.EventType.BUTTON_PRESS:
			if self.turn in (4, 8, 12, 16, 20, 24, 28, 32, 36, 40):
				pass
			elif self.turn > 0:
				self.guesses[self.turn // 4].pop()
				self.turn -= 1
				self.image_panel[self.turn][0].set_from_file(self.color.get_color(0))


main = MainWindow()
main.show_all()
main.connect("delete-event", Gtk.main_quit)
Gtk.main()
