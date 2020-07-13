# -----------------------------------------------------------------------------
# Name:        Add and remove exercise screen (addRemoveExercise.py)
# Purpose:     Creates the screen for adding and removing exercise events
#
# Author:      Abtin Tabrizi
# Created:     13-Jan-2020
# Updated:     16-Jan-2020
# -----------------------------------------------------------------------------
import kivy
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from popups.pREvent import PREvent
from popups.pEvent import PEvent
from objects.calEvent import CalEvent
from objects.exercise import Exercise
from objects.medication import Medication

def showPEvent():
    """
    Creates and runs the duplicate event popup

    Parameters
    ----------
    none

    Returns
    -------
    none
    """
    # Popup content
    show = PEvent()
    popupWindow = Popup(title="Date Error", content=show, size_hint=(0.85, 0.15), size=(0, 0))
    popupWindow.open()
    return

def showPREvent():
    """
    Creates and runs the nonexistant event popup

    Parameters
    ----------
    none

    Returns
    -------
    none
    """
    # Popup content
    show = PREvent()
    popupWindow = Popup(title="Event Error", content=show, size_hint=(0.85, 0.15), size=(0, 0))
    popupWindow.open()
    return


class AddRemoveExerciseWindow(Screen):
    """
    A class for creating the AddRemoveExerciseWindow screen

    Allows for the creation of the AddRemoveExerciseWindow screen in the .kv file

    Attributes
    ----------
    none

    Methods
    -------
    add() -> None
        Adds an exercise to user's file
    remove() -> None
        Removes an exercise from user's file
    """
    def add(self) -> None:
        """
        Adds a new exercise event to the user's calendar file

        Checks for a unique exercise event and adds it to the user specific calendar file

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        # Creating default variables
        exists = False
        eventList = []

        # Gets current account from file based on whether logged in or signed up
        file = open("logOrSign.txt", "r")
        info = file.readlines()
        file.close()
        if "0" in info:
            from screens.logInWindow import currentAccount
        if "1" in info:
            from screens.signUpWindow import currentAccount

        # Create/read from user file
        file = open(currentAccount + "calendar.txt", "a")
        file.close()
        file = open(currentAccount + "calendar.txt", "r")
        events = file.readlines()
        file.close()

        # Turns text into a list of usable text with calendar event objects, exercise objects and medication objects
        for i in range(0, len(events), 1):
            events[i] = events[i].split("; ")
            if events[i][0] == "c":
                eventList.append(CalEvent(events[i][1], events[i][2], events[i][3], events[i][4], events[i][5]))
            elif events[i][0] == "e":
                eventList.append(Exercise(events[i][1], events[i][2], events[i][3], events[i][4], events[i][5], events[i][6], events[i][7], int(events[i][8]), int(events[i][9])))
            elif events[i][0] == "m":
                eventList.append(Medication(events[i][1], events[i][2], events[i][3], events[i][4], events[i][5], events[i][6], events[i][7], float(events[i][8])))

        # Getting text from text boxes
        name = self.ids.name.text
        location = self.ids.location.text
        note = self.ids.note.text
        time = self.ids.time.text
        date = self.ids.date.text
        eName = self.ids.eName.text
        eType = self.ids.eType.text
        sets = self.ids.sets.text
        reps = self.ids.reps.text

        # Checks for unique time and date
        if len(name) == 0 or len(time) == 0 or len(date) == 0 or len(eName) == 0 or len(str(sets)) == 0 or len(str(reps)) == 0:
            exists = True
        else:
            for i in range(0, len(eventList), 1):
                if time == eventList[i].time and date == eventList[i].date:
                    exists = True

        # Adds if unique event
        if exists == True:
            # Displays popup if event not unique
            showPEvent()
        else:
            # Adds inputted information to file
            newEvent = "e; " + name + "; " + location + "; " + note + "; " + time + "; " + date + "; " + eName + "; " + eType + "; " + str(sets) + "; " + str(reps) + "; \n"
            file = open(currentAccount + "calendar.txt", "a")
            file.write(newEvent)
            file.close()

            # Clears text boxes
            self.ids.name.text = ""
            self.ids.location.text = ""
            self.ids.note.text = ""
            self.ids.time.text = ""
            self.ids.date.text = ""
            self.ids.eName.text = ""
            self.ids.eType.text = ""
            self.ids.sets.text = ""
            self.ids.reps.text = ""
        return

    def remove(self) -> None:
        """
        Removes a exercise event from the user's calendar file

        Checks for an existing exercise event and removes it from the user's file

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        # Creating default variables
        exists = False
        eventList = []

        # Gets current account from file based on whether logged in or signed up
        file = open("logOrSign.txt", "r")
        info = file.readlines()
        file.close()
        if "0" in info:
            from screens.logInWindow import currentAccount
        if "1" in info:
            from screens.signUpWindow import currentAccount

        # Create/Read user file
        file = open(currentAccount + "calendar.txt", "a")
        file.close()
        file = open(currentAccount + "calendar.txt", "r")
        events = file.readlines()
        file.close()

        # Turns text into a list of usable text with calendar event objects, exercise objects and medication objects
        for i in range(0, len(events), 1):
            events[i] = events[i].split("; ")
            if events[i][0] == "c":
                eventList.append(CalEvent(events[i][1], events[i][2], events[i][3], events[i][4], events[i][5]))
            elif events[i][0] == "e":
                eventList.append(Exercise(events[i][1], events[i][2], events[i][3], events[i][4], events[i][5], events[i][6], events[i][7], int(events[i][8]), int(events[i][9])))
            elif events[i][0] == "m":
                eventList.append(Medication(events[i][1], events[i][2], events[i][3], events[i][4], events[i][5], events[i][6], events[i][7], float(events[i][8])))

        # Gets text from text boxes
        time = self.ids.time.text
        date = self.ids.date.text

        # Checks for existing time and date
        for i in range(0, len(eventList), 1):
            if events[i][0] == "e":
                if time == eventList[i].time and date == eventList[i].date:
                    exists = True
                    events[i] = ""
                    dontWrite = i

        # Updates user information or gives popup
        if exists == True:
            pass
            # Clears text files
            file = open(currentAccount + "calendar.txt", "w")
            file.write("")
            file.close()

            # Rewrites file with updated information
            for i in range(0, len(events), 1):
                if i != dontWrite:
                    if events[i][0] == "c":
                        event = events[i][0] + "; " + events[i][1] + "; " + events[i][2] + "; " + events[i][3] + "; " + events[i][4] + "; " + events[i][5] + "; \n"
                    elif events[i][0] == "e":
                        event = events[i][0] + "; " + events[i][1] + "; " + events[i][2] + "; " + events[i][3] + "; " + events[i][4] + "; " + events[i][5] + "; " + events[i][6] + "; " + events[i][7] + "; " + str(events[i][8]) + "; " + str(events[i][9]) + "; \n"
                    elif events[i][0] == "m":
                        event = events[i][0] + "; " + events[i][1] + "; " + events[i][2] + "; " + events[i][3] + "; " + events[i][4] + "; " + events[i][5] + "; " + events[i][6] + "; " + events[i][7] + "; " + str(events[i][8]) + "; \n"
                    file = open(currentAccount + "calendar.txt", "a")
                    file.write(event)
                    file.close()

            # Clears text boxes
            self.ids.name.text = ""
            self.ids.location.text = ""
            self.ids.note.text = ""
            self.ids.time.text = ""
            self.ids.date.text = ""
            self.ids.eName.text = ""
            self.ids.eType.text = ""
            self.ids.sets.text = ""
            self.ids.reps.text = ""
        else:
            # Displays error popup
            showPREvent()
        return
