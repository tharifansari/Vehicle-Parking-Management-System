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
        
class MainStaffSub(Frame):


    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initui()


    def initui(self):
        self.parent.title("STAFF CHOICE")
        button = Button(self, text="Entry", highlightbackground="black", command=self.subentry)
        button.grid(row=0)
        button1 = Button(self, text="Exit", highlightbackground="black", command=self.subexit)
        button1.grid(row=4)
        button2 = Button(self, text="LOG-OUT", highlightbackground="black", command=self.bckhm)
        button2.grid(row=6)
        self.pack()


    def bckhm(self):
        root.deiconify()
        self.parent.destroy()


    def subentry(self):
        self.parent.withdraw()
        global root8
        root8 = Tk()
        root8.geometry("1440x900")
        app1 = MainStaffEntry(root8)


    def subexit(self):
        root9 = Tk()
        self.parent.withdraw()
        root9.geometry("1440x900")
        app1 = MainStaffExit(root9)



class MainStaffEntry(Frame):


    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.one = ttk.Entry(self)
        self.two = ttk.Entry(self)
        self.three = ttk.Entry(self)
        self.four = ttk.Entry(self)
        self.five = ttk.Entry(self)
        self.six = ttk.Entry(self)
        self.seven = ttk.Entry(self)
        self.eight = ttk.Entry(self)
        self.nine = ttk.Entry(self)
        self.ten = ttk.Entry(self)
        self.parent = parent
        self.initui()


    def add(self):
        a = self.one.get()
        b = self.two.get()
        c = self.three.get()
        d = self.four.get()
        e = self.five.get()
        f = self.six.get()
        g = self.seven.get()
        h = self.eight.get()
        i = self.nine.get()
        j = self.ten.get()
        entry(a, b, c, d, e, f, g, h, i, j)


    def bckhm(self):
        self.parent.withdraw()
        root10.deiconify()


    def initui(self):
        self.parent.title("ENTRY")
        TICKET_NO = Label(self, text="TICKET NUMBER")
        EMP_ID = Label(self, text="EMPLOYEE ID")
        VEH_NUM = Label(self, text="VEHICLE NUMBER")
        ENTRY_TIME = Label(self, text="ENTRY TIME(hh:mm)")
        EXIT_TIME = Label(self, text="APPROXIMATE EXIT TIME(hh:mm)")
        ENTRY_DATE = Label(self, text="ENTRY DATE(yyyy:mm:dd)")
        NAME = Label(self, text="NAME")
        PHONE_NUM = Label(self, text="PHONE NUMBER")
        ADDRESS = Label(self, text="ADDRESS")
        VEH_TYPE = Label(self, text="VEHICLE TYPE")
        EMP_ID.grid(row=0)
        NAME.grid(row=2)
        VEH_NUM.grid(row=4)
        VEH_TYPE.grid(row=6)
        PHONE_NUM.grid(row=8)
        ADDRESS.grid(row=10)
        TICKET_NO.grid(row=12)
        ENTRY_TIME.grid(row=14)
        EXIT_TIME.grid(row=16)
        ENTRY_DATE.grid(row=18)
        self.one.grid(row=1)
        self.two.grid(row=3)
        self.three.grid(row=5)
        self.four.grid(row=7)
        self.five.grid(row=9)
        self.six.grid(row=11)
        self.seven.grid(row=13)
        self.eight.grid(row=15)
        self.nine.grid(row=17)
        self.ten.grid(row=19)
        button_for_batch = Button(self, text="ENTER", highlightbackground="black", command=self.add)
        button_for_batch.grid(row=20)
        button_for_batch1 = Button(self, text="BACK", highlightbackground="black", command=self.bckhm)
        button_for_batch1.grid(row=21)
        self.pack()


class MainStaffExit(Frame):


    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.vehnum = ttk.Entry(self)
        self.time = ttk.Entry(self)
        self.parent = parent
        self.initui()


    def subexit(self):
        vehnum = self.vehnum.get()
        time = self.time.get()
        exitt(vehnum, time)


    def bck(self):
        self.parent.withdraw()
        root10.deiconify()


    def initui(self):
        self.parent.title("EXIT DETAILS")
        one = Label(self, text="VEHICLE NUMBER")
        one.grid(row=0)
        self.vehnum.grid(row=1)
        two = Label(self, text="OUT TIME")
        two.grid(row=2)
        self.time.grid(row=3)
        button = Button(self, text="PROCEED", highlightbackground="black", command=self.subexit)
        button.grid(row=4)
        button = Button(self, text="BACK", highlightbackground="black", command=self.bck)
        button.grid(row=5)
        self.pack() 
