#-----------------------------------------------------------------------------
# Name:        Measurement class (measurement.py)
# Purpose:     Class for creating measurement objects
#
# Author:      Abtin Tabrizi
# Created:     06-Jan-2020
# Updated:     16-Jan-2020
#-----------------------------------------------------------------------------
class Measurement():
    """
    Creates measurement objects

    Creates measurement objects that store information on date, time and measurement

    Attributes
    ----------
    date : str
        The date of the measurement
    time : str
        The time of the measurement
    measurement : float
        The blood sugar measurement

    Methods
    -------
    none
    """
    def __init__(self, date, time, measurement):
        """
        A constructor for measurement objects

        Constructs a measurement object with information for date, time and measurement

        Parameters
        ----------
        date : str
            The date of the measurement
        time : str
            The time of the measurement
        measurement : float
            The blood sugar measurement

        Returns
        -------
        none
        """
        self.date = date
        self.time = time
        self.measurement = measurement