#/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Author: Goncalo Bejinha 13428
#

import sys
from Tkinter import *
import gui_tkinter
from gui_tkinter import*

class LoginMenu(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("340x130+500+300")
        self.title("Login")
        self.tries = 3 # see, we define your counter as a member of LoginMenu and initialize it here

        # these are the text boxes we'll want access to
        self.entryPass = StringVar()
        self.entryUser = StringVar()
        self.msgText = StringVar()
        
        # The objects on our form, but we really don't need to track them
        Label(self, text = "Username: ").place(x = 50, y = 12)
        Entry(self, textvariable = self.entryUser).place(x = 120, y = 13)
        
        Label(self, text = "Password: ").place(x = 58, y = 32)
        Entry(self, textvariable = self.entryPass).place(x = 120, y = 33)
        Button(self, text = "Login", command = self.login).place(x = 150, y = 90)

        # don't keep creating objects in the same place
        # just replace the text in the object
        Label(self, textvariable = self.msgText).place(x = 110, y = 58)

    def login(self):
        a = self.entryPass.get()
        b = self.entryUser.get()
        if (a != "maia" and b != "abelha"):
            # rather than creating a new object
            # tryLabel = Label(self, text = "You have %d tries left." %(self.tries)).place(x = 110, y = 58)
            self.tries -= 1
            # we'll just replace the text
            self.msgText.set("You have %d tries left." %(self.tries))
            if self.tries<1:
                self.destroy()
        else:
            # successLabel = Label(loginMenu, text = "Sucessfully login." ).place(x = 110, y = 58)
            self.msgText.set("Sucessfully login.")
            #self.destroy()
            gui_tkinter.main()
            

LoginMenu().mainloop()

