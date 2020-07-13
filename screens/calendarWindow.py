#-----------------------------------------------------------------------------
# Name:        Calendar screen (calendarWindow.py)
# Purpose:     Creates the calendar screen for the app
#
# Author:      Abtin Tabrizi
# Created:     19-Dec-2019
# Updated:     16-Jan-2020
#-----------------------------------------------------------------------------
import kivy
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.uix.screenmanager import Screen

import calendar
import datetime
from objects.calEvent import CalEvent
from objects.medication import Medication
from objects.exercise import Exercise

global check
check = False

def monthName(month):
	"""
	Determines the name of the month

	Determines name of month based on month number from datetime class

	Parameters
	----------
	month : int
		The number of the month from 1-12

	Returns
	-------
	name : string
		The string name of the month
	"""
	if month == 1:
		name = "January"
	elif month == 2:
		name = "February"
	elif month == 3:
		name = "March"
	elif month == 4:
		name = "April"
	elif month == 5:
		name = "May"
	elif month == 6:
		name = "June"
	elif month == 7:
		name = "July"
	elif month == 8:
		name = "August"
	elif month == 9:
		name = "September"
	elif month == 10:
		name = "October"
	elif month == 11:
		name = "November"
	elif month == 12:
		name = "December"
	return name


class CalendarWindow(Screen):
	"""
	A class for creating the CalendarWindow screen

    Allows for the creation of the CalendarWindow screen in the .kv file
	
	Attributes
	----------
	none
		
	Methods
	-------
	refresh() -> None
		Displays current date and updates calendar information
	previous() -> None
		Displays the previous month
	next() -> None
		Displays the next month
	"""
	def refresh(self) -> None:
		"""
        Updates information and displays current month

        Checks user information and displays a calendar based on the current Gregorian month

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
		# Gets current year and month and creates a check to keep program from breaking
		current = datetime.datetime.now()
		global year
		year = current.year
		global month
		month = current.month
		global check
		check = True

		# Gets name of the month
		mName = monthName(month)

		# Creates text
		self.canvas.add(Color(0.49803921568, 0.692, 0.98039215686, 1))
		self.canvas.add(Rectangle(pos=(100, 100), size=(200, 700)))
		self.canvas.add(Rectangle(pos=(0, 100), size=(1000, 350)))
		date = Label(text=mName + " " + str(year), pos_hint={"x": 0.45, "top": 0.85}, size_hint=(0.1, 0.1), font_size=25, color=(0, 0, 0, 1))
		self.add_widget(date)
		return

	def previous(self):
		"""
        Shows previous month's information

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
		# Checks for the page to have been refreshed
		global check
		if check == True:
			# Gets current month and year
			global month
			global year

			# Moves back a month
			month = month - 1
			if month == 0:
				year = year - 1
				month = 12

			# Gets name of the month
			mName = monthName(month)

			# Creates text
			self.canvas.add(Color(0.49803921568, 0.692, 0.98039215686, 1))
			self.canvas.add(Rectangle(pos=(100, 100), size=(200, 700)))
			self.canvas.add(Rectangle(pos=(0, 100), size=(1000, 350)))
			date = Label(text=mName + " " + str(year), pos_hint={"x": 0.45, "top": 0.85}, size_hint=(0.1, 0.1), font_size=25, color=(0, 0, 0, 1))
			self.add_widget(date)
		else:
			# Creates text
			self.canvas.add(Color(0.49803921568, 0.692, 0.98039215686, 1))
			self.canvas.add(Rectangle(pos=(0, 100), size=(1000, 350)))
			message = Label(text="Please refresh first", pos_hint={"x": 0.45, "top": 0.45}, size_hint=(0.1, 0.1), font_size=25, color=(0, 0, 0, 1))
			self.add_widget(message)
		return

	def next(self) -> None:
		"""
        Shows next month's information

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
		# Checks for the page to have been refreshed
		global check
		if check == True:
			# Gets current month and year
			global year
			global month

			# Moves month forward
			month = month + 1
			if month == 13:
				year = year + 1
				month = 1

			# Gets name of the month
			mName = monthName(month)

			# Creates text
			self.canvas.add(Color(0.49803921568, 0.692, 0.98039215686, 1))
			self.canvas.add(Rectangle(pos=(100, 100), size=(200, 700)))
			self.canvas.add(Rectangle(pos=(0, 100), size=(1000, 350)))
			date = Label(text=mName + " " + str(year), pos_hint={"x": 0.45, "top": 0.85}, size_hint=(0.1, 0.1), font_size=25, color=(0, 0, 0, 1))
			self.add_widget(date)
		else:
			# Creates text
			self.canvas.add(Color(0.49803921568, 0.692, 0.98039215686, 1))
			self.canvas.add(Rectangle(pos=(0, 100), size=(1000, 350)))
			message = Label(text="Please refresh first", pos_hint={"x": 0.45, "top": 0.45}, size_hint=(0.1, 0.1), font_size=25, color=(0, 0, 0, 1))
			self.add_widget(message)
		return