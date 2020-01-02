from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import re
import admin
import staff
import staff
from PIL import Image, ImageTk


def dat(date):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    dbms = db.cursor()
    try:
        dbms.execute("select sum(amount) from tot_trans_day where date=%s group by date", date)
        res = dbms.fetchone()
        var = res[0]
        var = str(var)
        tkinter.messagebox.showinfo(" ", ("TOTAL TRANSACTION " + var))
        db.commit()
    except:
        db.rollback()
        tkinter.messagebox.showerror("ERROR OCCURED IN READING THE DATABASE\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")
    db.close()


def removeempp(empid):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    dbms = db.cursor()
    try:
        dbms.execute("delete from employee where emp_id=%s", (empid))
        tem = str(empid)
        tem = tem + " is removed successfully "
        tkinter.messagebox.showinfo(" ", " Employee with id " + tem)
        db.commit()
    except:
        db.rollback()
        tkinter.messagebox.showerror("Error ocuured in reading the database\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")
    db.close()


def count_proc(date):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    dbms = db.cursor()
    try:
        dbms.execute("CALL COST2(%s, @val)", (date))
        res = dbms.fetchone()
        var = res[0]
        if var > 0:
            var = str(var)
            tkinter.messagebox.showinfo("", (" COUNT OF VEHICLES PARKED IS " + var))
        else:
            tkinter.messagebox.showinfo(" ", ("NO VEHICLES PARKED ON " + date))
        db.commit()
    except:
        db.rollback()
        tkinter.messagebox.showerror(" ERROR OCCURED IN READING THE DATABASE\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")
    db.close()


def check_veh(veh_num):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    allow = db.cursor()
    try:
        allow.execute("select veh_num from vehicle_owner")
        result = allow.fetchall()
        flag = 0
        for i in result:
            if i.__contains__(veh_num) == 1:
                flag = 1
                break
            else:
                flag = 0
        db.commit()
    except:
        db.rollback()
        tkinter.messagebox.showerror("ERROR OCCURED IN READING THE DATABASE\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")
    db.close()
    if flag == 1:
        return TRUE
    else:
        return FALSE


def check_admin(name, passcode):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    allrows = db.cursor()
    try:
        allrows.execute("select name from admin")
        results = allrows.fetchall().__str__()
        allrows1 = db.cursor()
        allrows1.execute("select passcode from admin")
        results1 = allrows1.fetchall().__str__()
        flag = 0
        if results.__contains__(name):
            if results1.__contains__(passcode):
                flag = 1
        else:
            flag = 0
        db.commit()
    except:
        db.rollback()
        tkinter.messagebox.showerror("ERROR OCCURED IN READING THE DATABASE\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")
    db.close()
    if flag == 1:
        return TRUE
    else:
        return FALSE


def check_staff(id, passcode):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    allrows = db.cursor()
    try:
        allrows.execute("select emp_id from employee")
        results = allrows.fetchall()
        allrows1 = db.cursor()
        allrows1.execute("select passcode from employee")
        results1 = allrows1.fetchall().__str__()
        flag = 0
        db.commit()
        for i in results:
            if i.__contains__(id):
                if results1.__contains__(passcode):
                    flag = 1
                    break
                else:
                    flag = 0
    except:
        db.rollback()
        tkinter.messagebox.showerror("ERROR OCCURED IN READING THE DATABASE\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")
    db.close()
    if flag == 1:
        return TRUE
    else:
        return FALSE


def addstaff(a, b, c, d, e):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    hey = db.cursor()
    try:
        hey.execute("insert into employee values(%s, %s, %s, %s ,%s)", (a, b, c, d, e))
        tem = str(a)
        tem = tem + ' '
        tkinter.messagebox.showinfo(" ", b + " WAS ADDED SUCCESSFULLY WITH ID NO " + tem)
        db.commit()
    except:
        db.rollback()
        tkinter.messagebox.showerror("Error occured in reading the database\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")
    db.close()


def cost_calculation(veh_num):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    hey = db.cursor()
    try:
        hey.execute("select out_time,in_time from parking where veh_num=%s", (veh_num))
        res = hey.fetchall().__str__()
        res1 = res.split()
        text = res1[0]
        m = re.search('seconds=(.+)\)', text)
        if m:
            found = m.group(1)
        start = int(found)
        text = res1[1]
        m = re.search('seconds=(.+)\)\)', text)
        if m:
            found = m.group(1)
        end = int(found)
    except:
        db.rollback()
        tkinter.messagebox.showerror("Error occured in reading the database\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")
    db.close()
    return (((start-end)/3600)*15)


def entry(a, b, c, d, e, f, g, h, i, j):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    hey = db.cursor()
    try:
        hey.execute("insert into VEHICLE_OWNER values(%s, %s, %s, %s ,%s)", (c, b, e, f, d))
        db.commit()
        hey.execute("insert into parking values(%s, %s, %s, %s, %s, %s)", (g, a, c, h, i, j))
        tkinter.messagebox.showinfo(" ", "Vehicle is added successfully")
        global clean_res
        clean_res = tkinter.messagebox.askyesno("Vehicle cleaning ", " Does the customer wanted his vehicle to be cleaned")
        tkinter.messagebox.showinfo(" ", "Rupees 150 will be added to the final cost\nTHANK YOU")
        db.commit()
    except:
        db.rollback()
        tkinter.messagebox.showerror("Error occured in reading the database\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")
    db.close()


def exitt(vehnum, time):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    hey = db.cursor()
    try:
        res = check_veh(vehnum)
        if res != TRUE:
            tkinter.messagebox.showwarning("WRONG VEHICLE NUMBER", "NO VEHICLE WITH SUCH REG NUM IS PARKED")
        else:
            hey.execute("desc parking")
            hey.execute("update parking set out_time =%s where veh_num = %s ", (time, vehnum))
            db.commit()
            cost = cost_calculation(vehnum)
            if tkinter.messagebox.askyesno("TICKET", "TICKET SHOWN") == 0:
                tkinter.messagebox.showinfo(" ", "RUPEES 100 WILL BE ADDED TO THE FINAL COST")
                cost = cost + 100
                t_lost(vehnum)

            if clean_res == 1:
                cost = cost + 150
                v_cleaning(vehnum)

            cost1 = str(cost)
            tkinter.messagebox.showinfo(" ", "COST TO BE PAID AT THE COUNTER IS " + cost1)
            tran(vehnum, cost)
    except:
        db.rollback()
        tkinter.messagebox.showerror("Error occured in reading the database\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")


def tran(vehnum, cost):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    dbms = db.cursor()
    try:
        dbms.execute("select ticket_num, in_date, emp_id from parking where veh_num =%s", (vehnum))
        res = dbms.fetchone()
        tic_num = res[0]
        date = res[1]
        empid = res[2]
        dbms.execute("insert into transactions values(%s, %s, %s, %s, %s)", (tic_num, date, empid, vehnum, cost))
        db.commit()
    except:
        db.rollback()
        tkinter.messagebox.showerror("Error occured in reading the database\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")
    db.close()


def t_lost(vehnum):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    dbms = db.cursor()
    try:
        dbms.execute("select emp_id from parking where veh_num =%s", (vehnum))
        res = dbms.fetchone()
        empid = res[0]
        dbms.execute("insert into ticket_lost values (%s, %s)", (empid, vehnum))
        db.commit()
    except:
        db.rollback()
        tkinter.messagebox.showerror("Error occured in reading the database\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")
    db.close()


def v_cleaning(vehnum):
    db = pymysql.connect("localhost", "root", "your_password", "database_name")
    dbms = db.cursor()
    try:
        dbms.execute("select ticket_num, emp_id from parking where veh_num =%s", (vehnum))
        res = dbms.fetchone()
        tic_num = res[0]
        empid = res[1]
        dbms.execute("insert into vehicle_cleaning values (%s, %s, %s)", (tic_num, empid, vehnum))
        db.commit()
    except:
        db.rollback()
        tkinter.messagebox.showerror("Error occured in reading the database\nPLEASE GO TO CONSOLE TO VIEW THE ERROR")
    db.close()


class MainClass(Frame):


    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initui()


    def calladmin(self):
        root11 = Tk()
        root11.geometry("1440x900")
        app = MainAdmin(root11)


    def callcust(self):
        root12 = Tk()
        root12.geometry("1440x900")
        app2 = MainCustomer(root12)


    def callstaff(self):
        root13 = Tk()
        root13.geometry("1440x900")
        app1 = MainStaff(root13)


    def initui(self):
        self.parent.title("SELECTION OF USER")
        button_for_batch = Button(self, text="ADMIN LOG_IN", highlightbackground="black", command=self.calladmin)
        button_for_batch.grid(row=2, columnspan=2)
        button_it = Button(self, text="CUSTOMER QUERY", highlightbackground="black", command=self.callcust)
        button_it.grid(row=3, columnspan=2)
        button_it = Button(self, text="STAFF LOG_IN", highlightbackground="black", command=self.callstaff)
        button_it.grid(row=4, columnspan=2)
        button_for_batch1 = Button(self, text="QUIT", highlightbackground="black", command=exit)
        button_for_batch1.grid(row=5, columnspan=2)
        self.pack()


root = Tk()
# to have a full screen page use Root.gmty(value x value) inside paranthesis is x not *
root.geometry("1440x900")
root.title('Parking System')
img = ImageTk.PhotoImage(Image.open("lambo.jpeg"))
panel = Label(root, image=img)
panel.pack()
app = MainClass(root)
root.mainloop()
