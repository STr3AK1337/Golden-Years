#-----------------------------------------------------------------------------
# Name:        App For Seniors (main.py)
# Purpose:     An app with many functions helpful for seniors
#
# Author:      Abtin Tabrizi
# Created:     12-Sep-2019
# Updated:     12-Sep-2019
#-----------------------------------------------------------------------------
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(GridLayout):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    email = ObjectProperty(None)

    def but(self):
        information = self.username.text + " " + self.password.text + " " + self.email.text + "\n"
        self.username.text = ""
        self.password.text = ""
        self.email.text = ""
        file = open('C:/Users/Abtin/Desktop/comp sci/users.txt', 'a')
        file.write(information)
        file.close()


class FilesApp(App):
    def build(self):
        return MyGrid() 


if __name__ == "__main__":
    FilesApp().run()