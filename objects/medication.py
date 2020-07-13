#-----------------------------------------------------------------------------
# Name:        Medication class (medication.py)
# Purpose:     Class for creating medication objects
#
# Author:      Abtin Tabrizi
# Created:     30-Dec-2019
# Updated:     17-Jan-2020
#-----------------------------------------------------------------------------
from objects.calEvent import CalEvent


class Medication(CalEvent):
    """
    Creates medication objects

    Creates medication objects that store information on name of medication, type of medication and dosage and also extends the calEvent class

    Attributes
    ----------
    mName : str
        The name of the medication
    mType : str
        The type of medication (pill, injection etc...)
    dose : float
        The dosage of the medication

    Methods
    -------
    none
    """
    def __init__(self, name, location, note, time, date, mName, mType, dose):
        """
        A constructor for medication objects

        Constructs a medication object with information for name of medication, type of medication and dosage that also extends the calEvent class

        Parameters
        ----------
        mName : str
            The name of the medication
        mType : str
            The type of medication (pill, injection etc...)
        dose : float
            The dosage of the medication

        Returns
        -------
        none
        """
        super().__init__(name, location, note, time, date)
        self.mName = mName
        self.mType = mType
        self.dose = dose