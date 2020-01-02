from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import re
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


# classes related to ADMIN
# ------------------------------------------------------------------------------------------------------------

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


# classes related to CUSTOMER
# ------------------------------------------------------------------------------------------------------------

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



# classes related to Staff
# ------------------------------------------------------------------------------------------------------------


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
