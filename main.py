from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import tkinter.font as tkFont
import pymysql
import staffdet
import menudet
import billing
import createuserid
import customerdatabase
import userdatabase
import help
import sys
import base64

def main():
    root = Tk()
    app = LoginPage(root)
    root.mainloop()

class LoginPage:

    def __init__(self, root):

        # SOME IMPORTANT FUNCTIONS -------------------------------------------
        
        def connect2db():
            # To connect to the database
            self.mydb = pymysql.connect(
                        host="localhost", user="root", password="", database="rms")
            self.curs = self.mydb.cursor()

        def enddb():
            # To end the connection to the database
            self.mydb.commit()
            self.mydb.close()

        def fetchappname():
            connect2db()
            self.curs.execute(
                "SELECT Keyvalue FROM `otherdetails` WHERE `id` LIKE 'appname'")
            secdata = self.curs.fetchall()
            enddb()
            if len(secdata) != 0:
                temp = secdata[0][0]
            return temp
        
        # BASIC STRUCTURE -----------------------------------------------------

        appname = fetchappname()
        self.root = root

        self.root.state('zoomed')

        self.root.maxsize(1300, 650)
        self.root.minsize(1300, 650)

        self.root.title(appname)
        self.root.configure(background="ivory2")
        self.title_lbl = Label(self.root, text=f"{appname} - Dashboard",
                               bg="lightgrey", relief=GROOVE, font="calibri 13 bold")
        self.title_lbl.pack(fill=X, side=TOP)

        self.loginfrm = Frame(self.root, bg="lightgrey", bd=6, relief=GROOVE)
        self.loginfrm.place(x=390, y=120, width=500, height=368)

        self.logintitle = Label(self.loginfrm, text="Login", bg="lightgrey",
                                font="TimesNewRoman 15 bold", anchor=CENTER, bd=4, relief=GROOVE)
        self.logintitle.pack(fill=X, side=TOP)

        self.entryfrm = LabelFrame(
            self.loginfrm, text="Enter Details:", bd=4, bg="lightgrey", font="sans-serif 10")
        self.entryfrm.place(x=0, y=33, height=322, width=488)

        # FONTS------------------------------------------------------------------
        helv11 = tkFont.Font(family="Helvetica",size=11,weight="normal")
        helv10 = tkFont.Font(family="Helvetica",size=10,weight="normal")

        # VARIABLES-------------------------------------------------------------

        username = StringVar()
        password = StringVar()

        # USERNAME PASSWORD FRAME, LABEL AND ENTRY---------------------------------

        self.logindetfrm = Frame(self.entryfrm, bg="lightgrey", relief=GROOVE)
        self.logindetfrm.place(x=20, y=25)

        self.usernamelbl = Label(
            self.logindetfrm, text="Username:", bg="lightgrey", font=helv11)
        self.usernamelbl.grid(row=0, column=0, pady=10, padx=15)

        self.usernameentry = Entry(
            self.logindetfrm, textvariable=username, bd=3, relief=GROOVE, font=helv10)
        self.usernameentry.grid(row=0, column=1, ipadx=10, ipady=3)

        self.passwordlbl = Label(
            self.logindetfrm, text="Password:", bg="lightgrey", font=helv11)
        self.passwordlbl.grid(row=1, column=0, pady=10, padx=15)

        self.passwordentry = Entry(
            self.logindetfrm, textvariable=password, bd=3, relief=GROOVE, show="*", font=helv10)
        self.passwordentry.grid(row=1, column=1, padx=5, ipadx=10, ipady=3)

        # FUNCTIONS---------------------------------------------------------
    
        def logout():
            # To logout the account
            self.billingbtn.config(state=DISABLED)
            self.menubtn.config(state=DISABLED)
            self.staffbtn.config(state=DISABLED)
            self.createidbtn.config(state=DISABLED)
            self.customerdbbtn.config(state=DISABLED)
            self.userdbbtn.config(state=DISABLED)
            reset()
            self.loginbtn.config(text="Log In", command=checklogin)

        def checklogin():
            # To verify username and password and take necessary actions
            if username.get() and password.get():
                try:
                    connect2db()
                    self.curs.execute(
                        "SELECT `username`, `password` FROM `logindetails` WHERE `username` LIKE %s", (username.get()))
                    content = self.curs.fetchall()
                    
                    if len(content) != 0:
                        value = content[0][1]
                        
                        if password.get() == value:
                            self.billingbtn.config(state=NORMAL)
                            self.menubtn.config(state=NORMAL)
                            self.staffbtn.config(state=NORMAL)
                            self.createidbtn.config(state=NORMAL)
                            self.customerdbbtn.config(state=NORMAL)
                            self.userdbbtn.config(state=NORMAL)
                            self.loginbtn.config(
                                text="Log Out", command=logout)

                        else:
                            messagebox.showerror(
                                "Error!", "Invalid Credentials.", parent=self.root)

                    else:
                        messagebox.showerror(
                            "Error!", "User does not exist!", parent=self.root)

                    enddb()

                except Exception as e:
                    messagebox.showerror(
                        "Connection Error!", "User could not be verified, Please try again later.", parent=self.root)

            elif not username.get() and password.get():
                messagebox.showerror(
                    "Error!", "Please enter a valid username.", parent=self.root)
                
            elif username.get() and not password.get():
                messagebox.showerror(
                    "Error!", "Please enter your password.", parent=self.root)
                
            else:
                messagebox.showerror(
                    "Error!", "Please enter the credentials.", parent=self.root)

        def reset():
            # To reset the entry fields
            username.set("")
            password.set("")

        def billing_section():
            # To open Billing Window
            self.newwindow = Toplevel(self.root)
            self.app = billing.BillingWindow(self.newwindow)

        def staff_list():
            # To open Staff List Window
            self.newwindow = Toplevel(self.root)
            self.app = staffdet.Staff(self.newwindow)

        def helpfunc():
            # To open Help Winowd
            self.newwindow = Toplevel(self.root)
            self.app = help.HelpEmailer(self.newwindow)
            
        def createid():
            # To open Create ID Window
            self.newwindow = Toplevel(self.root)
            self.app = createuserid.NewUser(self.newwindow)

        def menuopen():
            # To open Menu Window
            self.newwindow = Toplevel(self.root)
            self.app = menudet.MenuPage(self.newwindow)

        def custdb():
            # To open Customer Database Window
            self.newwindow = Toplevel(self.root)
            self.app = customerdatabase.CustomerDB(self.newwindow)

        def useriddbopen():
            # To open System User Database Window
            self.newwindow = Toplevel(self.root)
            self.app = userdatabase.UseridDB(self.newwindow)

        # DASHBOARD BUTTONS AND FRAME--------------------------------------

        self.btnfrm = Frame(self.entryfrm, bg="lightgrey", relief=GROOVE)
        self.btnfrm.place(x=35, y=143)

        self.loginbtn = Button(self.btnfrm, text="Log In", bd=4,
                               relief=GROOVE, width=13, height=1, command=checklogin)
        self.loginbtn.grid(row=0, column=0, padx=10, pady=5, ipadx=5, ipady=3)

        self.billingbtn = Button(self.btnfrm, text="Billing", bd=4, relief=GROOVE, width=13, height=1,
                                 state=DISABLED, command=billing_section)
        self.billingbtn.grid(row=0, column=1, padx=10,pady=5, ipadx=5, ipady=3)

        self.resetbtn = Button(self.btnfrm, text="Reset", bd=4,
                               relief=GROOVE, width=13, height=1, command=reset)
        self.resetbtn.grid(row=0, column=2, padx=10, pady=5, ipadx=5, ipady=3)

        self.menubtn = Button(self.btnfrm, text="Menu", bd=4,
                              relief=GROOVE, width=13, height=1, command=menuopen, state=DISABLED)
        self.menubtn.grid(row=1, column=0, padx=10, pady=5, ipadx=5, ipady=3)

        self.staffbtn = Button(self.btnfrm, text="Staff Details",
                               bd=4, relief=GROOVE, width=13, height=1, command=staff_list, state=DISABLED)
        self.staffbtn.grid(row=1, column=1, padx=10, pady=5, ipadx=5, ipady=3)
        
        self.createidbtn = Button(self.btnfrm, text="Create New User", bd=4,
                              relief=GROOVE, width=13, height=1, command=createid, state=DISABLED)
        self.createidbtn.grid(row=1, column=2, padx=10, pady=5, ipadx=5, ipady=3)

        self.userdbbtn = Button(self.btnfrm, text="User Database", bd=4,
                              relief=GROOVE, width=13, height=1, command=useriddbopen, state=DISABLED)
        self.userdbbtn.grid(row=2, column=0, padx=10, pady=5, ipadx=5, ipady=3)

        self.customerdbbtn = Button(self.btnfrm, text="Customer Database", bd=4,
                              relief=GROOVE, width=13, height=1, command=custdb, state=DISABLED)
        self.customerdbbtn.grid(row=2, column=1, padx=10, pady=5, ipadx=5, ipady=3)

        self.helpbtn = Button(self.btnfrm, text="Help", bd=4,
                              relief=GROOVE, width=13, height=1, command=helpfunc)
        self.helpbtn.grid(row=2, column=2, padx=10, pady=5, ipadx=5, ipady=3)


        # -----------------------------------FOOTER-----------------------------------------
        self.footer_lbl = Label(self.root, text="CHIRANJEEV SEHGAL ©",
                                bg="lightgrey", relief=GROOVE, font="calibri 8 bold")
        self.footer_lbl.pack(fill=X, side=BOTTOM)

# ------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()