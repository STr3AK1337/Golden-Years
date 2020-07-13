#-----------------------------------------------------------------------------
# Name:        Blood sugar screen (bloodSugarWindow.py)
# Purpose:     Creates the blood sugar window for the app
#
# Author:      Abtin Tabrizi
# Created:     30-Dec-2019
# Updated:     16-Jan-2020
#-----------------------------------------------------------------------------
import kivy
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.uix.screenmanager import Screen

import datetime
import operator
from objects.measurement import Measurement


class BloodSugarWindow(Screen):
    """
	A class for creating the BloodSugarWindow screen

    Allows for the creation of the BloodSugarWindow screen in the .kv file
	
	Attributes
	----------
	none
		
	Methods
	-------
	show(average, recent, recentDate) -> None
        Displays the average and recent blood sugar measurements
    refresh() -> None
        Averages the most recent measurements and updates information
	"""
    def show(self, average, recent, recentDate) -> None:
        """
        Creates text on screen

        Displays average and recent data on screen

        Parameters
        ----------
        average : float
            The average blood sugar over the most recent existing days
        recent: float
            The most recently added measurement
        recentDate: str
            The date of the most recently added measurement

        Returns
        -------
        none
        """
        # Creates text on screen
        self.canvas.add(Color(0.49803921568, 0.692, 0.98039215686, 1))
        self.canvas.add(Rectangle(pos=(0, 125), size=(10000, 350)))
        recentAverage = Label(text="Ten day average is: " + str(round(average, 2)), pos_hint={"x": 0.45, "top": 0.55}, size_hint=(0.1, 0.1), font_size= 25, color=(0, 0, 0, 1))
        self.add_widget(recentAverage)
        mostRecent = Label(text="Last measurement: " + str(recent), pos_hint={"x": 0.45, "top": 0.45}, size_hint=(0.1, 0.1), font_size= 25, color=(0, 0, 0, 1))
        self.add_widget(mostRecent)
        mostRecentDate = Label(text="Added on: " + recentDate, pos_hint={"x": 0.45, "top": 0.4}, size_hint=(0.1, 0.1), font_size= 25, color=(0, 0, 0, 1))
        self.add_widget(mostRecentDate)
        return

    def refresh(self) -> None:
        """
        Gets recent averages for blood sugar and updates information

        Takes available data for the ten most recent inputs of blood sugar and averages them

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        # Setting default variables
        measurementList = []
        avgList = []
        total = 0
        average = 0
        recent = 0
        recentDate = "None"

        # Gets current account from file based on whether the user logged in or signed up
        file = open("logOrSign.txt", "r")
        info = file.readlines()
        file.close()
        if "0" in info:
            from screens.logInWindow import currentAccount
        elif "1" in info:
            from screens.signUpWindow import currentAccount

        # Gets information or creates files
        file = open(currentAccount + "bsugar" + ".txt", "a")
        file.close()
        file = open(currentAccount + "bsugar" + ".txt", "r")
        measurements = file.readlines()
        file.close()

        # Turns text into usable text and creates a list of measurement objects
        for i in range(0, len(measurements), 1):
            measurements[i] = measurements[i].split("; ")
            measurementList.append(Measurement(measurements[i][0], measurements[i][1], measurements[i][2]))

        # Bubble sorting the list
        """
        sorted = False
        while sorted == False:
            sorted = True
            for i in range(0, len(measurementList)-1, 1):
                if measurementList[i].date > measurementList[i+1].date:
                    sorted = False
                    hold = measurementList[i+1]
                    measurementList[i+1] = measurementList[i]
                    measurementList[i] = hold
                elif measurementList[i].date == measurementList[i+1].date:
                    if measurementList[i].time > measurementList[i+1].time:
                        sorted = False
                        hold = measurementList[i+1]
                        measurementList[i+1] = measurementList[i]
                        measurementList[i] = hold
        """
        # Took 25 seconds for a 177kb file
        # Took 2 minutes for a 354kb file

        # Insertion sorting the list
        """
        for i in range(1, len(measurementList), 1): 
            key = measurementList[i].date
            key2 = measurementList[i].time
            hold = measurementList[i]
            j = i-1
            otherKey = measurementList[j].date
            otherKey2 = measurementList[j].time
            if key < otherKey:
                while j >= 0 and key < otherKey : 
                    measurementList[j + 1] = measurementList[j] 
                    j = j - 1
                measurementList[j + 1] = hold
            elif key == otherKey:
                while j >= 0 and key2 < otherKey2 : 
                    measurementList[j + 1] = measurementList[j] 
                    j = j - 1
                measurementList[j + 1] = hold
        """
        # Took 18 seconds for a 354kb file
        # Took 1 minute 23 seconds for a 708kb file

        # Sorts the measurement objects by date and time with .sort()
        measurementList.sort(key = operator.attrgetter("date", "time"))
        # Took 39 milliseconds for a 708kb file
        # Took 75 milliseconds for a 1.38mb file
        # Took 1 second 83 milliseconds for a 41.5mb file

        # Binary searching the sorted file
        """
        start = 0
        end = len(measurementList) - 1
        while start < end:
            middle = start + (end-start)/2
            middle = int(middle)
            if measurementList[middle].date == "2023/08/21" and measurementList[middle].time == "07:19":
                middle = middle + 1
                print(str(middle))
                break
            elif measurementList[middle].date < "2023/08/21":
                start = middle + 1
            elif measurementList[middle].date == "2023/08/21" and measurementList[middle].time < "07:19":
                start = middle + 1
            else:
                end = middle - 1
        """
        # Took 10.581 milliseconds for a 273kb file
        # Took 25.002 milliseconds for a 546kb file
    
        # Linear searching unsorted file
        """
        for i in range(0, len(measurementList), 1):
            if measurementList[i].date == "2023/08/21" and measurementList[i].time == "07:19":
                print(i)
        """
        # Took 4.221 milliseconds for a 273kb file
        # Took 4.324 milliseconds for a 546kb file

        # Calculates averages
        if len(measurementList) >= 10:
            recentDate = measurementList[-1].date + " at " + measurementList[-1].time
            recent = measurementList[-1].measurement
            for i in range(len(measurementList)-1, len(measurementList)-11, -1):
                avgList.append(measurementList[i].measurement)
            for i in range(0, len(avgList), 1):
                total = total + (float(avgList[i]))
            average = total/10
        elif len(measurementList) > 0 and len(measurementList) < 10:
            recentDate = measurementList[-1].date + " at " + measurementList[-1].time
            recent = measurementList[-1].measurement
            for i in range(len(measurementList)-1, -1, -1):
                if i != -1:
                    avgList.append(measurementList[i].measurement)
            for i in range(0, len(avgList), 1):
                total = total + (float(avgList[i]))
            average = total/len(avgList)

        # Runs the show() function to display information
        self.show(average, recent, recentDate)
        return