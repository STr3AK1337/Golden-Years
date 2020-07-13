#-----------------------------------------------------------------------------
# Name:        Sign up screen (signUpWindow.py)
# Purpose:     Creates the sign up screen for the app
#
# Author:      Abtin Tabrizi
# Created:     30-Dec-2019
# Updated:     16-Jan-2020
#-----------------------------------------------------------------------------
import kivy
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from objects.users import Users
from popups.pEmail import PEmail
from popups.pUsername import PUsername

userList = []

def showPUsername():
    """
    Creates and runs the incorrect username popup

    Parameters
    ----------
    none

    Returns
    -------
    none
    """
    # Popup content
    show = PUsername()
    popupWindow = Popup(title="Username Error", content=show, size_hint=(0.75,0.15),size=(0,0)) 
    popupWindow.open()
    return
    
def showPEmail():
    """
    Creates and runs the incorrect email popup

    Parameters
    ----------
    none

    Returns
    -------
    none
    """
    # Popup content
    show = PEmail()
    popupWindow = Popup(title="Email Error", content=show, size_hint=(0.75,0.15),size=(0,0)) 
    popupWindow.open()
    return


class SignUpWindow(Screen):
    """
	A class for creating the SignUpWindow screen

    Allows for the creation of the sign up screen in the .kv file
	
	Attributes
	----------
	none
		
	Methods
	-------
	signUp() -> None
        Signs the user up and creates account
	"""
    def signUp(self) -> None:
        """
        Signs the user up for the app

        Creates an account for the user and makes sure that it is unique

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        # Sets default variables
        usernameExists = False
        emailExists = False

        # Gets text from textboxes
        user = self.ids.username.text
        passw = self.ids.password.text
        email = self.ids.email.text

        # Creates/Reads information from files
        file = open("logOrSign.txt", "a")
        file.close()
        file = open("users.txt", "a")
        file.close()
        file = open("users.txt", "r")
        userInfo = file.readlines()
        file.close()

        # Converts each user into usable lists of data and adds user objects to a list for later use
        for i in range(0, len(userInfo), 1):
            userInfo[i] = userInfo[i].split("; ")
            userList.append(Users(userInfo[i][0], userInfo[i][1], userInfo[i][2]))

        # Checks for unique accounts
        for i in range(0, len(userInfo), 1):
            if user == userInfo[i][0]:
                usernameExists = True 
            if email == userInfo[i][2]:
                emailExists = True

        # Gives error popups for existing accounts and signs in for new accounts
        if usernameExists == True:
            showPUsername()
        elif emailExists == True:
            showPEmail()
        elif usernameExists == False and emailExists == False:
            # For use in other files tells user signed up
            file = open("logOrSign.txt", "w")
            file.write("1")
            file.close()

            # Global variable for program to access user specific files
            global currentAccount
            currentAccount = str(user)
    
            # Adds the accounts to the file that stores all users
            store = str(user) + "; " + str(passw) + "; " + str(email) + "; \n"
            file = open("users.txt", "a")
            file.write(store)
            file.close()

            # Empties text boxes and goes to main screen
            self.ids.username.text = ""
            self.ids.password.text = ""
            self.ids.email.text = ""
            self.manager.current = "main"
        return