#-----------------------------------------------------------------------------
# Name:        Window manager (windowManager.py)
# Purpose:     Allows for the changing of screens
#
# Author:      Abtin Tabrizi
# Created:     18-Dec-2019
# Updated:     16-Jan-2020
#-----------------------------------------------------------------------------
import kivy
from kivy.uix.screenmanager import Screen, ScreenManager

from screens.signUpWindow import SignUpWindow
from screens.logInWindow import LogInWindow
from screens.mainWindow import MainWindow
from screens.calendarWindow import CalendarWindow
from screens.addRemoveCalEventWindow import AddRemoveCalEventWindow
from screens.addRemoveExerciseWindow import AddRemoveExerciseWindow
from screens.addRemoveMedicationWindow import AddRemoveMedicationWindow
from screens.bloodSugarWindow import BloodSugarWindow
from screens.bloodSugarRemoveWindow import BloodSugarRemoveWindow
from screens.bloodSugarAddWindow import BloodSugarAddWindow


class WindowManager(ScreenManager):
    """
	A class that manages the different screens

    Allows for code in the .kv file to switch between all the different screens
	
	Attributes
	----------
	none
		
	Methods
	-------
	none
	"""
    pass