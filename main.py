#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
from src.checker.checker import Checker
from src.generator.generator import Generator
from time import time


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Secret Code")

        self.turn = 0
        self.set_default_size(550, 550)
        self.number_of_guesses = 10
        self.Y_STEP = 60
        self.button_size = 50
        self.secret_code = Generator.create()
        self.code = []
        self.secret_code_status = False
        self.get_time = lambda: int(round(time() * 1000))
        self.last_time = self.get_time()
        fixed = Gtk.Fixed()
        fixed.put(self.add_buttons(), 0, 0)
        fixed.put(self.add_options(), 10, 50)
        fixed.put(self.add_secret_code(), 100, 50)
        fixed.put(self.add_code_panel(), 100, 110)
        fixed.put(self.add_guess_panel(), self.button_size * 7, 110)
        self.add(fixed)

    def get_colors(self, color):
        return {
            0: "imgs/default.png",
            1: "imgs/red.png",
            2: "imgs/yellow.png",
            3: "imgs/green.png",
            4: "imgs/orange.png",
            5: "imgs/pink.png",
            6: "imgs/purple.png",
            7: "imgs/blue.png",
            8: "imgs/white.png",
        }.get(color, None)

    def add_options(self):
        """
        Just creates the color palette for options
        """
        frame = Gtk.Frame()
        fixed = Gtk.Fixed()

        for color in range(1, 9):
            obj = Gtk.Image()
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.get_colors(color), 50, 50, False)
            obj.set_from_pixbuf(pixbuf)
            fixed.put(obj, 0, -60 + 60 * color)

        eventBox = Gtk.EventBox()
        eventBox.add(fixed)
        eventBox.connect("button-press-event", self.clicked_options)

        frame.add(eventBox)
        return frame

    def add_secret_code(self):
        """"
        Just creates the Secret Code
        """
        frame = Gtk.Frame()
        fixed = Gtk.Fixed()
        self.secret_panel = []
        x_step = 0
        for i in range(0, 4):
            tempImage = Gtk.Image()
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.get_colors(0), self.button_size, self.button_size,
                                                             False)
            tempImage.set_from_pixbuf(pixbuf)
            self.secret_panel.append([tempImage, 0 + x_step, 0])
            x_step += self.button_size * 1.2

        for image in self.secret_panel:
            fixed.put(image[0], image[1], image[2])

        frame.add(fixed)
        return frame

    def add_code_panel(self):
        """"Creates the code Entry Panel"""
        frame = Gtk.Frame()
        fixed = Gtk.Fixed()
        self.code_panel = []
        y_step = 0
        for z in range(0, self.number_of_guesses):
            x_step = 0
            for i in range(0, 4):
                tempImage = Gtk.Image()
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.get_colors(0), self.button_size, self.button_size, False)
                tempImage.set_from_pixbuf(pixbuf)
                self.code_panel.append([tempImage, 0 + x_step, y_step])
                x_step += self.button_size * 1.2
            y_step += self.Y_STEP

        for image in self.code_panel:
            fixed.put(image[0], image[1], image[2])

        event_box = Gtk.EventBox()
        event_box.add(fixed)
        event_box.connect("button-press-event", self.clicked_code_panel)

        frame.add(event_box)
        return frame

    def add_guess_panel(self):
        """Creates the guess panel"""
        frame = Gtk.Frame()
        fixed = Gtk.Fixed()
        self.guess_panel = []
        size = 15
        y_step = 0
        for z in range(0, self.number_of_guesses):
            x_step = 0
            for i in range(0, 4):
                temp = Gtk.Image()
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.get_colors(0), self.button_size, self.button_size, False)
                temp.set_from_pixbuf(pixbuf)
                self.guess_panel.append([temp, 0 + x_step, y_step])
                x_step += self.button_size * 1.2
            y_step += self.Y_STEP

        for image in self.guess_panel:
            fixed.put(image[0], image[1], image[2])
        frame.add(fixed)
        return frame

    def add_buttons(self):
        """Creates buttons"""
        fixed = Gtk.Fixed()
        buttonReset = Gtk.Button("Reset")
        buttonReset.connect("clicked", self.clicked_reset)
        buttonToggle = Gtk.Button("Toggle")
        buttonToggle.connect("clicked", self.clicked_toggle)

        fixed.put(buttonReset, 10, 10)
        fixed.put(buttonToggle, 110, 10)

        return fixed

    def is_double_click(self):
        """Returns True if it is a double_click, else False"""
        current_time = self.get_time()
        result = current_time - self.last_time < 10
        self.last_time = current_time
        return result

    def clicked_reset(self, widget):
        """Resets secret code, doesn't show it. Remove code and guesses"""
        self.new_secret_code()
        self.remove_all_code_and_guesses()

    def clicked_options(self, eventbox, event):
        """Handler for options_panel clicked"""
        if self.is_double_click():
            return
        for color in range(1, 9):
            if int(event.y // 60) == color - 1:
                self.code_panel[self.turn][0].set_from_file(self.get_colors(color))
                self.add_code(color)

    def clicked_code_panel(self, eventbox, event):
        """Handler for code_panel clicked"""
        # Validate through y
        y0 = (self.turn // 4) * self.Y_STEP
        ymax = y0 + self.button_size
        if not (y0 <= int(event.y) <= ymax):
            return

        # Validate through x
        for index in range(0, 4):
            x0 = index * (self.button_size * 1.2)
            xmax = x0 + self.button_size
            if x0 <= int(event.x) <= xmax:
                self.remove_code(index)

    def clicked_toggle(self, widget):
        """Handler for toggle button clicked"""
        self.show_secret_code()

    def update_code(self, values):
        """Updates current turn's code"""
        code = values[:]
        current_length = len(code)
        for i in range(4 - current_length):
            code.append(0)

        for i in range(4):
            self.code_panel[(self.turn // 4) * 4 + i][0].set_from_file(self.get_colors(code[i]))

    def remove_all_code_and_guesses(self):
        """Removes all code and guesses from panels"""
        for j in range(self.number_of_guesses):
            for i in range(4):
                self.code_panel[j * 4 + i][0].set_from_file(self.get_colors(0))
                self.guess_panel[j * 4 + i][0].set_from_file(self.get_colors(0))
        self.turn = 0
        self.code = []

    def update_guesses(self, values):
        """Updates guesses panel"""
        for i in range(4):
            self.guess_panel[self.turn - 4 + i][0].set_from_file(self.get_colors(values[i]))

    def update_secret_code(self, values):
        """Updates secret code panel"""
        for i in range(4):
            self.secret_panel[i][0].set_from_file(self.get_colors(values[i]))

# Logic starts here
    def new_secret_code(self):
        """Creates a new code. Do not show it."""
        self.secret_code = Generator.create()
        self.show_secret_code(force=False)

    def check_guesses(self, guesses):
        """
        Check current code with secret code,
        Update guesses panel,
        Reset current code,
        Check for win hand.
        """
        if self.turn % 4 == 0:
            values = Checker(self.secret_code).check_code(guesses)
            self.update_guesses(values)
            self.code = []

            if all(value == 1 for value in values):
                self.show_secret_code(force=True)

    def show_secret_code(self, force=None):
        """
        Toggle to show secret code
        :param force: If it is set to True, is shown, to False is not shown
        """
        self.secret_code_status = not self.secret_code_status if force is None else force
        values = [0] * 4 if not self.secret_code_status else self.secret_code
        self.update_secret_code(values)

    def add_code(self, color):
        """Add color to current code"""
        self.code.append(color)
        self.turn += 1
        self.check_guesses(self.code)

    def remove_code(self, position):
        """Remove position from current code, and update code."""
        try:
            self.code.pop(position)
            self.turn -= 1
            self.update_code(self.code)
        except IndexError:
            pass

mainwindow = MainWindow()
mainwindow.show_all()
mainwindow.connect("delete-event", Gtk.main_quit)
Gtk.main()
