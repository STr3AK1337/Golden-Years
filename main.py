#-----------------------------------------------------------------------------
# Name:        Main file for app (main.py)
# Purpose:     Runs the app with helpful functions for seniors
#
# Author:      Abtin Tabrizi
# Created:     12-Sept-2019
# Updated:     16-Jan-2020
#-----------------------------------------------------------------------------
import kivy
from kivy.app import App
from kivy.lang import Builder

from screens.windowManager import WindowManager

kv = Builder.load_file("main.kv")


class MainApp(App):
    """
    Creates the usable GUI of the app

    Uses App from the kivy framework to create the usable GUI of the application

    Attributes
    ----------
    none

    Methods
    -------
    build() -> kv
        Creates the usable GUI of the program 
    """
    def build(self) -> kv:
        """
        Loads the test.kv file

        Loads the test.kv file which creates the GUI and its functionality

        Parameters
        ----------
        none

        Returns
        -------
        file
           Returns the test.kv file so the code can make use of it  
        """
        # Connects to the .kv file
        return kv


# Start of program
if __name__ == "__main__":
    MainApp().run()

# Finite data has has a countable amount of data that can be stored in the computer. 
# A computer does not have an infite amount of storage so there can never be an infinite amount of data stored. 
# This means that something like a decimal cannot have an infinite amount of decimal places stored or a list can't have an infinite amount of items. 
# When storing numbers as decimals this means that the number will never be perfectly accurate.