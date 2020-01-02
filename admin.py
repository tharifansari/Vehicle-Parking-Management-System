from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import re
from PIL import Image, ImageTk

class MainAdmin(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        root.withdraw()
        self.three = ttk.Entry(self)
        self.four = ttk.Entry(self, show="*")
        self.parent = parent
        self.initui()

    def admin_acpt(self):
        a = self.three.get()
        b = self.four.get()
        res = check_admin(a, b)
        if res == TRUE:
            tkinter.messagebox.showinfo(" ", " SUCCESSFUL LOGIN")
            self.parent.withdraw()
            global root1
            root1 = Tk()
            root1.geometry("1440x900")
            app1 = MainAdmin1(root1)
        else:
            tkinter.messagebox.showinfo("LOG-IN FAILED", "INVALID CREDENTIALS \nNAME/PASSCODE is wrong\nPlease try again ")

    def bckhm(self):
        self.parent.withdraw()
        root.deiconify()

    def initui(self):
        self.parent.title("ADMIN LOG IN")
        one = Label(self, text="ADMIN NAME")
        two = Label(self, text="PASSCODE")
        one.grid(row=0)
        two.grid(row=2)
        self.three.grid(row=1)
        self.four.grid(row=3)
        button_for_batch = Button(self, text="SUBMIT", highlightbackground="black", command=self.admin_acpt);
        button_for_batch.grid(row=4)
        button_for_batch1 = Button(self, text="BACK", highlightbackground="black", command=self.bckhm);
        button_for_batch1.grid(row=5)
        self.pack()


class MainAdmin1(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initui()

    def initui(self):
        self.parent.title("ADMIN'S CHOICE")
        button_for_batch1 = Button(self, text="ADD AN EMPLOYEE", highlightbackground="black", command=self.addemployee)
        button_for_batch1.grid(row=0)
        button_for_batch2 = Button(self, text="REMOVE AN EMPLOYEE", highlightbackground="black", command=self.removee)
        button_for_batch2.grid(row=2)
        button_for_batch3 = Button(self, text="VIEW TOTAL TRANSACTION OF A PARTICULAR DAY", highlightbackground="black", command=self.everyday)
        button_for_batch3.grid(row=4)
        button_for_batch4 = Button(self, text="COUNT VEHICLE PARKED IN A PARTICULAR DAY", highlightbackground="black", command=self.count)
        button_for_batch4.grid(row=6)
        button_for_batch5 = Button(self, text="LOGOUT", highlightbackground="black", command=self.bckhm)
        button_for_batch5.grid(row=8)
        self.pack()


    def bckhm(self):
        self.parent.withdraw()
        root.deiconify()


    def count(self):
        self.parent.withdraw()
        root3 = Tk()
        root3.geometry("1440x900")
        app4 = MainSub3(root3)


    def addemployee(self):
        self.parent.withdraw()
        global root4
        root4 = Tk()
        root4.geometry("1440x900")
        app1 = MainSubAdd(root4)


    def removee(self):
        self.parent.withdraw()
        root5 = Tk()
        root5.geometry("1440x900")
        app2 = MainSub1(root5)


    def everyday(self):
        self.parent.withdraw()
        root6 = Tk()
        root6.geometry("1440x900")
        app3 = MainSub2(root6)


class MainSubAdd(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.one = ttk.Entry(self)
        self.two = ttk.Entry(self)
        self.three = ttk.Entry(self,show='*')
        self.four = ttk.Entry(self)
        self.five = ttk.Entry(self)
        self.parent = parent
        self.initui()


    def add(self):
        a = self.one.get()
        b = self.two.get()
        c = self.three.get()
        d = self.four.get()
        e = self.five.get()
        addstaff(a, b, c, d, e)


    def initui(self):
        self.parent.title("ADDING AN EMPLOYEE")
        EMP_ID = Label(self, text="ASSIGN AN EMPLOYEE ID")
        NAME = Label(self, text="NAME")
        PASSCODE = Label(self, text="PASSCODE")
        PHONE_NO = Label(self, text="PHONE")
        ADDRESS = Label(self, text="ADDRESS")
        EMP_ID.grid(row=0)
        NAME.grid(row=2)
        PASSCODE.grid(row=4)
        PHONE_NO.grid(row=6)
        ADDRESS.grid(row=8)
        self.one.grid(row=1)
        self.two.grid(row=3)
        self.three.grid(row=5)
        self.four.grid(row=7)
        self.five.grid(row=9)
        button_for_batch = Button(self, text="SUBMIT", highlightbackground="black", command=self.add)
        button_for_batch.grid(row=10)
        button_for_batch1 = Button(self, text="BACK", highlightbackground="black", command=self.bck)
        button_for_batch1.grid(row=11)
        self.pack()


    def bck(self):
        self.parent.withdraw()
        root1.deiconify()


class MainSub1(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.one = ttk.Entry(self)
        self.parent = parent
        self.initui2()


    def initui2(self):
        self.parent.title("Removing an employee")
        empid = Label(self, text="Enter Employee ID ")
        empid.grid(row=0)
        self.one.grid(row=1)
        button_for_batch = Button(self, text="REMOVE", highlightbackground="black", command=self.remove)
        button_for_batch.grid(row=2)
        button_for_batch = Button(self, text="BACK", highlightbackground="black", command=self.bck)
        button_for_batch.grid(row=3)
        self.pack()


    def remove(self):
        a = self.one.get()
        removeempp(a)


    def bck(self):
        self.parent.withdraw()
        root1.deiconify()


class MainSub2(Frame):


    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.one = ttk.Entry(self)
        self.parent = parent
        self.initui3()


    def initui3(self):
        self.parent.title("TOTAL TRANSACTION OF A PARTICULAR DAY")
        empid = Label(self, text="Enter the DATE")
        empid.grid(row=0)
        self.one.grid(row=1)
        button_for_batch = Button(self, text="PROCEED", highlightbackground="black", command=self.ver)
        button_for_batch.grid(row=2)
        button_for_batch1 = Button(self, text="BACK", highlightbackground="black", command=self.bck)
        button_for_batch1.grid(row=3)
        self.pack()


    def ver(self):
        a = self.one.get()
        dat(a)


    def bck(self):
        self.parent.withdraw()
        root1.deiconify()


class MainSub3(Frame):


    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.date = ttk.Entry(self)
        self.initui()


    def initui(self):
        self.parent.title("COUNT")
        DATE = Label(self, text="DATE")
        DATE.grid(row=0)
        self.date.grid(row=1)
        button_for_batch = Button(self, text="COUNT", highlightbackground="black", command=self.add)
        button_for_batch.grid(row=3)
        button_for_batch1 = Button(self, text="BACK", highlightbackground="black", command=self.bck)
        button_for_batch1.grid(row=4)
        self.pack()


    def add(self):
        date = self.date.get()
        count_proc(date)


    def bck(self):
        self.parent.withdraw()
        root1.deiconify()
