#-----------------------------------------------------------------------------
# Name:        Blood sugar adding screen (bloodSugarAddWindow.py)
# Purpose:     Creates the blood sugar adding window for the app
#
# Author:      Abtin Tabrizi
# Created:     30-Dec-2019
# Updated:     16-Jan-2020
#-----------------------------------------------------------------------------
import kivy
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from objects.measurement import Measurement
from popups.pBSugar import PBSugar

def showPBSugar():
    """
    Creates and runs the duplicate measurement popup

    Parameters
    ----------
    none

    Returns
    -------
    none
    """
    # Popup content
    show = PBSugar()
    popupWindow = Popup(title="Date Error", content=show, size_hint=(0.85,0.15),size=(0,0)) 
    popupWindow.open()
    return


class BloodSugarAddWindow(Screen):
    """
	A class for creating the BloodSugarAddWindow screen

    Allows for the creation of the BloodSugarAddWindow screen in the .kv file
	
	Attributes
	----------
	none
		
	Methods
	-------
	add() -> None
        Adds the measurement to the user's file
	"""
    def add(self) -> None:
        """
        Adds a new measurement to measurement file

        Checks for a unique measurement and adds it to the user specific measurement file

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        # Set default variables
        exists = False
        measurementList = []

        # Gets current account from file based on whether the user logged in or signed up
        file = open("logOrSign.txt", "r")
        info = file.readlines()
        file.close()
        if "0" in info:
            from screens.logInWindow import currentAccount
        elif "1" in info:
            from screens.signUpWindow import currentAccount

        # Create/read from files
        file = open(currentAccount + "bsugar.txt", "a")
        file.close()
        file = open(currentAccount + "bsugar.txt", "r")
        measurements = file.readlines()
        file.close()

        # Converts text into usable text and creates a list of measurement objects
        for i in range(0, len(measurements), 1):
            measurements[i] = measurements[i].split("; ")
            measurementList.append(Measurement(measurements[i][0], measurements[i][1], measurements[i][2]))
        
        # Gets text from text boxes
        date = self.ids.date.text
        time = self.ids.time.text
        measurement = self.ids.measurement.text

        # Checks for unique information
        if len(date) == 0 or len(time) == 0 or len(measurement) == 0:
                exists = True
        else:
            for i in range(0, len(measurementList), 1):
                if date == measurementList[i].date and time == measurementList[i].time:
                    exists = True 
        
        # Gives result based on uniqueness of data
        if exists == True:
            # Displays error message popup
            showPBSugar()
        else:
            # Adds inputted information to file
            newMeasurement = str(date) + "; " + str(time) + "; " + str(measurement) + "; \n"
            file = open(currentAccount + "bsugar.txt", "a")
            file.write(newMeasurement)
            file.close()
            
            # Clears textboxes
            self.ids.date.text = ""
            self.ids.time.text = ""
            self.ids.measurement.text = ""
        return