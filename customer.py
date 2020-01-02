from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import re
from PIL import Image, ImageTk

class MainCustomer(Frame):


    def __init__(self, parent):
        Frame.__init__(self, parent)
        root.withdraw()
        self.two = ttk.Entry(self)
        self.parent = parent
        self.initui()


    def cust_verify(self):
        a = self.two.get().__str__()
        res = check_veh(a)
        if res == 1:
            root7 = Tk()
            root7.geometry("1440x900")
            root7.withdraw()
            app1 = customer_check(root7, a)
        else:
            temp = str(a)
            temp = temp + "\" IS PARKED\nPlease try again with valid REGISTRATION NUMBER"
            tkinter.messagebox.showinfo("QUERY FAILED", "NO VEHICLE WITH REGISTRATION NUMBER \"" + temp)


    def bckhme(self):
        root.deiconify()
        self.parent.destroy()


    def initui(self):
        self.parent.title("CUSTOMER QUERY")
        one = Label(self, text="VEHICLE NUMBER")
        one.grid(row=0)
        self.two.grid(row=1)
        button1 = Button(self, text="BACK TO HOME", highlightbackground="black", command=self.bckhme)
        button1.grid(row=4)
        button = Button(self, text="VERIFY", highlightbackground="black", command=self.cust_verify)
        button.grid(row=3)
        self.pack()


class customer_check(Frame):


    def __init__(self, parent, veh_num):
        Frame.__init__(self, parent)
        root.withdraw()
        self.parent = parent
        self.veh_num = veh_num
        self.initui()


    def initui(self):
        cost = cost_calculation(self.veh_num)
        temp = str(cost)
        tkinter.messagebox.showinfo(" ", "Cost is " + temp)
