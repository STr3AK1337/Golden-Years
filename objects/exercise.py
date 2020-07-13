#-----------------------------------------------------------------------------
# Name:        Exercise class (exercise.py)
# Purpose:     Class for creating exercise objects
#
# Author:      Abtin Tabrizi
# Created:     30-Dec-2019
# Updated:     17-Jan-2020
#-----------------------------------------------------------------------------
from objects.calEvent import CalEvent


class Exercise(CalEvent):
    """
    Creates exercise objects

    Creates exercise objects that store information on name of exercise, type of exercise, number of sets and reps and also extends the calEvent class

    Attributes
    ----------
    eName : str
        The name of the exercise
    eType : str
        The type of exercise (cardio, endurance etc...)
    sets : int
        The number of sets of the exercise to be completed
    reps : int
        The number of repetitions of the exercise to be completed for each set

    Methods
    -------
    none
    """
    def __init__(self, name, location, note, time, date, eName, eType, sets, reps):
        """
        A constructor for exercise objects

        Constructs an exercise object with information for name of exercise, type of exercise, number of sets and reps as well as extending the calEvent class

        Parameters
        ----------
        eName : str
            The name of the exercise
        eType : str
            The type of exercise (cardio, endurance etc...)
        sets : int
            The number of sets of the exercise to be completed
        reps : int
            The number of repetitions of the exercise to be completed for each set

        Returns
        -------
        none
        """
        super().__init__(name, location, note, time, date)
        self.eName = eName
        self.eType = eType
        self.sets = sets
        self.reps = reps