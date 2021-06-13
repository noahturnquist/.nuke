#Imports
import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout
env_is_nuke = True
try:
    import nuke
except ModuleNotFoundError:
    env_is_nuke = False

#Creating our class for our form which inherits from QDialog
class Form(QDialog):

    def __init__(self, parent = None):
        super(Form, self).__init__(parent) #Inheriting something from QDialog
        self.setWindowTitle("Noah's Form") #Setting the title of our window
        #Create widgets
        self.edit = QLineEdit("Write my name here...")  #Create a QLineEdit which is a space for user to input text
        self.button = QPushButton("Show Greetings")     #Create a button
        #Create a layout and add widgets
        layout = QVBoxLayout()      #Setup a basic layout where when widgets are assigned they appear top to bottom
        layout.addWidget(self.edit)     #Add our line input widget
        layout.addWidget(self.button)   #Add our button
        #Set dialog layout
        self.setLayout(layout)      #Setup our final layout to be displayed in application
        self.button.clicked.connect(self.greetings)     #Connect button to greetings method

    def greetings(self):
        print("Hello {}".format(self.edit.text()))      #Steal the input from self.edit widget and print it
        self.setWindowTitle("%s Form" % self.edit.text())   #Assign that same name to our window title


if __name__ == '__main__':
    if env_is_nuke:
        dialog = Form()
        dialog.show()
    else:
        app = QtWidgets.QApplication(sys.argv)
        dialog = Form()
        dialog.exec_()

    
def start():
    global dialog
    dialog = Form()
    dialog.show()

nuke.menu('Nuke').addCommand("Pipeline/Shot Launcher", "shot_launcher.start()", "ctrl + shift + o", shortcutContext = 2)