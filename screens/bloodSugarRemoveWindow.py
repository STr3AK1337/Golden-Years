#-----------------------------------------------------------------------------
# Name:        Blood sugar removing screen (bloodSugarRemoveWindow.py)
# Purpose:     Creates the blood sugar removing window for the app
#
# Author:      Abtin Tabrizi
# Created:     30-Dec-2019
# Updated:     16-Jan-2020
#-----------------------------------------------------------------------------
import kivy
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from objects.measurement import Measurement
from popups.pRBSugar import PRBSugar

def showPRBSugar():
    """
    Creates and runs the nonexistant measurement popup

    Parameters
    ----------
    none

    Returns
    -------
    none
    """
    # Popup content
    show = PRBSugar()
    popupWindow = Popup(title="Measurement Does Not Exist", content=show, size_hint=(0.85,0.15),size=(0,0)) 
    popupWindow.open()
    return


class BloodSugarRemoveWindow(Screen):
    """
	A class for creating the BloodSugarRemoveWindow screen

    Allows for the creation of the BloodSugarRemoveWindow screen in the .kv file
	
	Attributes
	----------
	none
		
	Methods
	-------
	delete() -> None
        Deletes the selected measurement
	"""
    def delete(self) -> None:
        """
        Deletes a blood sugar measurement

        Deletes a user specific blood sugar measurement and updates the user's file

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        # Set default variable
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

        # Creates or reads files
        file = open(currentAccount + "bsugar" + ".txt", "a")
        file.close()
        file = open(currentAccount + "bsugar" + ".txt", "r")
        measurements = file.readlines()
        file.close()

        # Converts text into usable text and creates a list of measurement objects
        for i in range(0, len(measurements), 1):
            measurements[i] = measurements[i].split("; ")
            measurementList.append(Measurement(measurements[i][0], measurements[i][1], measurements[i][2]))        

        # Gets text from text boxes
        date = self.ids.date.text
        time = self.ids.time.text

        # Checks for measurement and removes it if it exists
        for i in range(0, len(measurementList), 1):
            if date == measurementList[i].date and time == measurementList[i].time:
                exists = True
                measurements[i] = ""
                dontWrite = i
        
        # Updates user information or gives error
        if exists == True:
            # Clears text file
            file = open(currentAccount + "bsugar.txt", "w")
            file.write("")
            file.close()

            # Rewrites text file with updated information
            for i in range(0, len(measurements), 1):
                if i != dontWrite:
                    item = measurements[i][0] + "; " + measurements[i][1] + "; " + measurements[i][2] + "; \n"
                    file = open(currentAccount + "bsugar.txt", "a")
                    file.write(item)
                    file.close()

            # Clears textboxes
            self.ids.date.text = ""
            self.ids.time.text = ""
        else:
            # Displays error popup
            showPRBSugar()
        return