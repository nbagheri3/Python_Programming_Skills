# ----------------------------------------------------------------------
# Name:        gui1
# Purpose:     Our first tkinter app
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module to demonstrate the steps involves in creating a GUI application.
"""
import tkinter  # step 1: import the tkinter module


def main():
    root = tkinter.Tk()  # step 2: create the application main window
    # add your code here
    root.title('CS 122') # customize the main window
    # instantiate a Label widget with root as the parent widget
    # use the text option to specify
    hello = tkinter.Label(root, text="Hello World!")
    hello.pack()
    root.mainloop()      # step 5: enter the main event loop and wait


if __name__ == '__main__':
    main()
