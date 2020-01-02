from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import re
from PIL import Image, ImageTk

class MainStaff(Frame):


    def __init__(self, parent):
        Frame.__init__(self, parent)
        root.withdraw()
        self.three1 = ttk.Entry(self)
        self.four1 = ttk.Entry(self, show="*")
        self.parent = parent
        self.initui()


    def staff_acpt(self):
        a = int(self.three1.get())
        b = self.four1.get()
        res = check_staff(a, b)
        if res == TRUE:
            self.parent.withdraw()
            global root10
            root10 = Tk()
            root10.geometry("1440x900")
            app1 = MainStaffSub(root10)
        else:
            tkinter.messagebox.showinfo("LOG-IN FAILED", "INVALID CREDENTIALS \nID/PASSCODE is wrong\nPlease try again ")


    def initui(self):
        self.parent.title("STAFF LOG-IN")
        one = Label(self, text="EMPLOYEE ID")
        two = Label(self, text="PASSCODE")
        one.grid(row=0)
        two.grid(row=2)
        self.three1.grid(row=1)
        self.four1.grid(row=3)
        button_for_batch = Button(self, text="SUBMIT", highlightbackground="black", command=self.staff_acpt)
        button_for_batch.grid(row=4)
        button_for_batch1 = Button(self, text="BACK", highlightbackground="black", command=self.bck)
        button_for_batch1.grid(row=5)
        self.pack()


    def bck(self):
        self.parent.destroy()
        root.deiconify()
