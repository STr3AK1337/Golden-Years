#-----------------------------------------------------------------------------
# Name:        Calendar Event class (calEvent.py)
# Purpose:     Class for creating calEvent objects
#
# Author:      Abtin Tabrizi
# Created:     30-Dec-2019
# Updated:     17-Jan-2020
#-----------------------------------------------------------------------------
class CalEvent():
    """
    Creates calendar event objects

    Creates calendar event objects with attributes for name, location, notes, time, and date

    Attributes
    ----------
    name : str
        The name of the event happening
    location : str
        The location of the calendar event
    note : str
        A note associated with the event
    time : str
        The time that the event will occur
    date : str
        The date that the event will occur

    Methods
    -------
    none
    """
    def __init__(self, name, location, note, time, date):
        """
        A constructor that builds a calendar event object

        Creates calendar event objects with attributes for name, location, notes, time, and date

        Parameters
        ----------
        name : str
            The name of the event happening
        location : str
            The location of the calendar event
        note : str
            A note associated with the event
        time : str
            The time that the event will occur
        date : str
            The date that the event will occur

        Returns
        -------
        none
        """
        self.name = name
        self.location = location
        self.note = note
        self.time = time
        self.date = date