# ----------------------------------------------------------------------
# Name:        gui2
# Purpose:     Our second tkinter app
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Module to demonstrate an object oriented GUI application.
"""
import tkinter


class GenApp:

    """
    class to support a general purpose GUI app

    Argument:
    parent: (tkinter.Tk) the root window object

    Attribute(s):
    status: (tkinter.Label) A Label widget showing the current
    """

    def __init__(self, parent):
        parent.title('CS 122')
        # create a START button and associate it with the start method
        start_button = tkinter.Button(parent, text='START', width=20,
                                      command=self.start)
        start_button.pack() # register it with a geometry manage
        # create a STOP button and associate it with the stop method
        stop_button = tkinter.Button(parent, text='STOP', width=20,
                                     command=self.stop)
        stop_button.pack() # register it with a geometry manage
        # create a status label to show the current status.
        self.status = tkinter.Label(parent, text='Ready to start')
        self.status.pack() # register it with a geometry

    def start(self):
        """
        update status label to show that the user has pressed
        the START button
        :return: None
        """
        self.status.configure(text='In progress', foreground='green')


    def stop(self):
        """
        update status label to show that the user has pressed
        the STOP button
        :return: None
        """
        self.status.configure(text='All Done!', foreground='red')


def main():
    root = tkinter.Tk()  # step 2: create the application main window
    gen_app = GenApp(root) # instantiate our generic App object
    root.mainloop()      # step 5: enter the main event loop and wait


if __name__ == '__main__':
    main()