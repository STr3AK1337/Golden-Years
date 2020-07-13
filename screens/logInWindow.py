#-----------------------------------------------------------------------------
# Name:        Log in screen (logInWindow.py)
# Purpose:     Creates the log in screen for the app
#
# Author:      Abtin Tabrizi
# Created:     19-Dec-2019
# Updated:     16-Jan-2020
#-----------------------------------------------------------------------------
import kivy
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from objects.users import Users
from popups.pLog import PLog

userList = []

def showPLog():
    """
    Creates and runs the incorrect login popup

    Parameters
    ----------
    none

    Returns
    -------
    none
    """
    # Popup content
    show = PLog()
    popupWindow = Popup(title="Username/Password Error", content=show, size_hint=(0.85,0.15),size=(0,0)) 
    popupWindow.open()
    return


class LogInWindow(Screen):
    """
	A class for creating the LogInWindow screen

    Allows for the creation of the LogInWindow screen in the .kv file
	
	Attributes
	----------
	none
		
	Methods
	-------
	logIn() -> None
        Logs the user in
	"""
    def logIn(self) -> None:
        """
        Logs the user in

        Checks for valid user credentials and logs them in

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        # Creates default variable
        match = False

        # Gets text from text inputs
        user = self.ids.username.text
        passw = self.ids.password.text

        # Creates and reads from file
        file = open("logOrSign.txt", "a")
        file.close()
        file = open("users.txt", "a")
        file.close()
        file = open("users.txt", "r")
        userInfo = file.readlines()
        file.close()

        # Converts fle data into usable lists of data and adds user objects to a list for later use
        for i in range(0, len(userInfo), 1):
            userInfo[i] = userInfo[i].split("; ")
            userList.append(Users(userInfo[i][0], userInfo[i][1], userInfo[i][2]))

        # Checks for existing account with valid credentials
        for i in range(0, len(userList), 1):
            if user == userList[i].username and passw == userList[i].password:
                match = True

        # Shows popup for incorrect account details
        if match == False:
            showPLog()
        else:
            # For use in other files tells user logged in
            file = open("logOrSign.txt", "w")
            file.write("0")
            file.close()

            # Global variable for use in other files
            global currentAccount
            currentAccount = str(user)

            # Empties text boxes and goes to main screen
            self.ids.username.text = ""
            self.ids.password.text = ""
            self.manager.current = "main"
        return