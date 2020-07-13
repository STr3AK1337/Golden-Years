#-----------------------------------------------------------------------------
# Name:        Users class (users.py)
# Purpose:     Class for creating user objects
#
# Author:      Abtin Tabrizi
# Created:     30-Dec-2019
# Updated:     16-Jan-2020
#-----------------------------------------------------------------------------
class Users():
    """
    Creates user objects

    Creates user objects that store information on username, password and email

    Attributes
    ----------
    username : str
        The user's  username
    password : str
        The user's password
    email : str
        The user's email

    Methods
    -------
    none
    """
    def __init__(self, username, password, email):
        """
        A constructor that builds a user object

        Constructs a user object with information for username, password and email

        Parameters
        ----------
        username : str
            The user's  username
        password : str
            The user's password
        email : str
            The user's email

        Returns
        -------
        none
        """
        self.username = username
        self.password = password
        self.email = email