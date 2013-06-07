#!/usr/bin/env python
"""
RacingPi gui initialisation
"""
import pygtk
pygtk.require("2.0")
import gtk

import game
import sys


VERBOSE_MODE = True

TITLE = "RacingPi"
TITLE_SIZE = 40000
DEFAULT_QUESTION = "What... is the air-speed velocity of an unladen swallow?"
QUESTION_SIZE = 12000
DEFAULT_SPACING = 10

RACING_PI_IMAGE = "racingpi/racingPi.png"


class RacingPiGUI(object):
	def __init__(self):
		self.the_game = None

		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("delete_event", self.delete_event)
		self.window.connect("destroy", self.destroy)
		self.window.set_border_width(10)
		self.window.set_title(TITLE)
		self.window.set_icon_from_file(RACING_PI_IMAGE)
		self.generate_contents()
		self.window.show()

	def delete_event(self, widget, data=None):
		return False # call the destroy event after this

	def destroy(self, widget, data=None):
		if self.the_game:
			self.the_game.stop()
		gtk.main_quit()

	def main(self):
		gtk.main()


	def generate_contents(self):
		"""Generates the contents of the window"""
		# label
		main_title = gtk.Label()
		main_title.set_use_markup(True)
		main_title.set_markup("<span size='%d'>%s</span>"%(TITLE_SIZE, TITLE))
		main_title.show()
		
		image = gtk.Image()
		image.set_from_file(RACING_PI_IMAGE)
		image.show()

		
		# question space
		self.question_label = gtk.Label()
		self.question_label.set_use_markup(True)
		self.update_question(DEFAULT_QUESTION)
		self.question_label.show()

		main_box = make_vbox(elements=[main_title, self.question_label])
		main_box.add(image)
		self.window.add(main_box)
		"""
		try:
			self.set_icon_from_file("racingPi.png")
		except Exception, e:
			print e.message
			sys.exit(1)	
		"""
	
	
	def update_question(self, new_question):
		# clean up question
		new_question = new_question.replace("<", "\<").replace(">", "/>")
		gtk.gdk.threads_enter()
		self.question_label.set_markup("<span size='%d'>%s</span>"%(QUESTION_SIZE, new_question))
		gtk.gdk.threads_leave()


def make_vbox(homogeneous=False, spacing=DEFAULT_SPACING, elements=(), expand=False):
	return make_box(gtk.VBox, homogeneous, spacing, elements, expand)

def make_hbox(homogeneous=False, spacing=DEFAULT_SPACING, elements=(), expand=False):
	return make_box(gtk.HBox, homogeneous, spacing, elements, expand)

def make_box(box_type, homogeneous, spacing, elements, expand):
	box = box_type(False, spacing)

	for element in elements:
		box.pack_start(element, expand)
		element.show()

	box.show()
	return box
