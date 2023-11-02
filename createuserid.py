from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import tkinter.font as tkFont
import pymysql
from random import randint
import smtplib
import ssl
from email.message import EmailMessage

def main():
    root = Tk()
    app = NewUser(root)
    root.mainloop()

class NewUser:

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

        # self.root.geometry("1200x600")
        self.root.state('zoomed')

        self.root.maxsize(1300, 650)
        self.root.minsize(1300, 650)

        self.root.title(appname)
        self.root.configure(background="ivory2")
        self.title_lbl = Label(self.root, text=f"{appname} - Create New User",
                               bg="lightgrey", relief=GROOVE, font="calibri 11 bold")
        self.title_lbl.pack(fill=X, side=TOP)

        self.signupfrm = Frame(self.root, bg="lightgrey", bd=6, relief=GROOVE)
        self.signupfrm.place(x=315, y=120, width=675, height=350)

        self.logintitle = Label(self.signupfrm, text="Signup", bg="lightgrey",
                                font="TimesNewRoman 11 bold", anchor=CENTER, bd=4, relief=GROOVE)
        self.logintitle.pack(fill=X, side=TOP)

        self.entryfrm = LabelFrame(
            self.signupfrm, text="Enter Details:", bd=4, bg="lightgrey", font="sans-serif 10")
        self.entryfrm.place(x=0, y=33, height=306, width=663)

        # FONTS------------------------------------------------------------------
        helv11 = tkFont.Font(family="Helvetica",size=11,weight="normal")
        helv10 = tkFont.Font(family="Helvetica",size=10,weight="normal")

        # VARIABLES-------------------------------------------------------------

        usernameinp = StringVar()
        nameinp = StringVar()
        passwordinp = StringVar()
        emailinp = StringVar()
        otpinp = StringVar()

        # USERNAME PASSWORD FRAME, LABEL AND ENTRY---------------------------------

        self.signupdetfrm = Frame(self.entryfrm, bg="lightgrey", relief=GROOVE)
        self.signupdetfrm.place(x=20, y=27)

        self.namelbl = Label(
            self.signupdetfrm, text="Name:", bg="lightgrey", font=helv11)
        self.namelbl.grid(row=0, column=0, pady=14, padx=15)

        self.nameentry = Entry(
            self.signupdetfrm, textvariable=nameinp, bd=3, relief=GROOVE, font=helv10)
        self.nameentry.grid(row=0, column=1, ipadx=10, ipady=3)
        
        self.emaillbl = Label(
            self.signupdetfrm, text="Email id:", bg="lightgrey", font=helv11)
        self.emaillbl.grid(row=0, column=2, pady=14, padx=15)

        self.emailentry = Entry(
            self.signupdetfrm, textvariable=emailinp, bd=3, relief=GROOVE, font=helv10)
        self.emailentry.grid(row=0, column=3, ipadx=10, ipady=3)

        self.usernamelbl = Label(
            self.signupdetfrm, text="Username:", bg="lightgrey", font=helv11)
        self.usernamelbl.grid(row=1, column=0, pady=14, padx=15)
        
        self.usernameentry = Entry(
            self.signupdetfrm, textvariable=usernameinp, bd=3, relief=GROOVE, font=helv10)
        self.usernameentry.grid(row=1, column=1, ipadx=10, ipady=3)

        self.passwordlbl = Label(
            self.signupdetfrm, text="Password:", bg="lightgrey", font=helv11)
        self.passwordlbl.grid(row=1, column=2, pady=14, padx=15)

        self.passwordentry = Entry(
            self.signupdetfrm, textvariable=passwordinp, bd=3, relief=GROOVE, show="*", font=helv10)
        self.passwordentry.grid(row=1, column=3, padx=5, ipadx=10, ipady=3)
        
        self.otplbl = Label(
            self.signupdetfrm, text="OTP:", bg="lightgrey", font=helv11)
        self.otplbl.grid(row=2, column=0, pady=14, padx=15)

        self.otpentry = Entry(
            self.signupdetfrm, textvariable=otpinp, bd=3, relief=GROOVE, font=helv10, state=DISABLED)
        self.otpentry.grid(row=2, column=1, padx=5, ipadx=10, ipady=3)

        # FUNCTIONS---------------------------------------------------------

        def fetchsenderemail():
            # To get the sender email id from the database
            connect2db()
            self.curs.execute(
                "SELECT Keyvalue FROM `otherdetails` WHERE `id` LIKE 'gmail_id'")
            secdata = self.curs.fetchall()
            enddb()
            if len(secdata) != 0:
                mail_id = secdata[0][0]
            return mail_id
        
        def fetchemailpassword():
            # To fetch the email app password from the database
            connect2db()
            self.curs.execute(
                "SELECT Keyvalue FROM `otherdetails` WHERE `id` LIKE 'gmailapp_pass'")
            secdata = self.curs.fetchall()
            enddb()
            if len(secdata) != 0:
                mail_pass = secdata[0][0]
            return mail_pass

        def otpgenerator():
            # To generate the otp
            self.otpgen = randint(100000, 999999)
            otpsend()

        def checkusernameavail():
            exists = False
            if nameinp.get() and emailinp.get() and usernameinp.get() and passwordinp.get():
            
                connect2db()
                self.curs.execute("SELECT * FROM `logindetails` WHERE `username` LIKE %s", {usernameinp.get()})
                tempdata = self.curs.fetchall()
                enddb()
                if len(tempdata) != 0:
                    exists = True
                
                if not exists:
                    otpgenerator()

                else:
                    messagebox.showerror(
                    "Error!", "Username already exists.", parent=self.root)

            else:
                    messagebox.showerror(
                        "Error!", "Please fill in the required information.", parent=self.root)

        def otpsend():
            # To send the email for otp
            
            # Sender email id
            email_sender = fetchsenderemail()

            # App password created after 2 step verification
            email_password = fetchemailpassword()

            # Receiver email id
            email_receiver = emailinp.get()

            otp = self.otpgen
            subject = "OTP Verification"
            body = f"Your OTP is {otp}."
            try:
                if nameinp.get() and usernameinp.get() and passwordinp.get() and emailinp.get():
                    em = EmailMessage()
                    em['From'] = email_sender
                    em['To'] = email_receiver
                    em['Subject'] = subject
                    em.set_content(body)

                    context = ssl.create_default_context()

                    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                        smtp.login(email_sender, email_password)
                        smtp.sendmail(
                            email_sender, email_receiver, em.as_string())
                        messagebox.showinfo(
                            "Success", "OTP has been successfully sent.", parent=self.root)
                        smtp.quit()
                        self.validateotpbtn.config(state=NORMAL)
                        self.sendotpbtn.config(
                                text="Resend OTP", command=otpgenerator)
                        self.validateotpbtn.config(state=NORMAL)
                        self.otpentry.config(state=NORMAL)
                        self.nameentry.config(state=DISABLED)
                        self.emailentry.config(state=DISABLED)
                        self.usernameentry.config(state=DISABLED)
                        self.passwordentry.config(state=DISABLED)

                else:
                    messagebox.showerror(
                        "Error!", "Please fill in the required information.", parent=self.root)

            except Exception as e:
                messagebox.showerror(
                    "Error!", "OTP could not be sent, Please try again later.", parent=self.root)
        
        def otpvalidate():
            # To validate the otp

            if otpinp.get():
                if otpinp.get() == str(self.otpgen):
                    registerfunc()

                elif otpinp.get() != str(self.otpgen):
                    messagebox.showerror(
                    "Error!", "Invalid OTP.", parent=self.root)
            else:
                messagebox.showerror(
                    "Empty!", "Please enter the OTP.", parent=self.root)

        def registerfunc():
            # To register the user
            
            try:
                    connect2db()
                    self.curs.execute("INSERT INTO logindetails (`SrNum`, `Name`,`Email`, `username`, `password`) VALUES(NULL,%s,%s,%s,%s)", (nameinp.get(), emailinp.get(), usernameinp.get(), passwordinp.get()))
                    
                    enddb()
                    messagebox.showinfo(
                        "Success", "User has been successfully added.", parent=self.root)
                    root.destroy()

            except Exception as e:
                    messagebox.showerror(
                        "Error!", "User cannot be added, Please try again later.", parent=self.root)
            
        def reset():
            # To reset all the fields

            nameinp.set("")
            emailinp.set("")
            usernameinp.set("")
            passwordinp.set("")
            otpinp.set("")
            self.validateotpbtn.config(state=DISABLED)
            self.otpentry.config(state=DISABLED)
            self.nameentry.config(state=NORMAL)
            self.emailentry.config(state=NORMAL)
            self.usernameentry.config(state=NORMAL)
            self.passwordentry.config(state=NORMAL)
            self.sendotpbtn.config( text="Send OTP", command=checkusernameavail)

        def exitfunc():
            # To exit
            
            root.destroy()


        # SIGNUP BUTTONS AND FRAME--------------------------------------

        self.btnfrm = Frame(self.entryfrm, bg="lightgrey", relief=GROOVE)
        self.btnfrm.place(x=120, y=204)

        self.sendotpbtn = Button(self.btnfrm, text="Send OTP", bd=4,
                               relief=GROOVE, width=13, height=1, command=checkusernameavail)
        self.sendotpbtn.grid(row=0, column=1, padx=10, pady=5, ipadx=5, ipady=3)

        self.validateotpbtn = Button(self.signupdetfrm, text="Validate OTP", bd=4,
                               relief=GROOVE, width=11, height=1, command=otpvalidate, state=DISABLED)
        self.validateotpbtn.grid(row=2, column=2, padx=20, pady=5, ipadx=2, ipady=1, columnspan=1)

        self.exitbtn = Button(self.btnfrm, text="Exit", bd=4, relief=GROOVE, width=13, height=1,
                                 state=NORMAL, command=exitfunc)
        self.exitbtn.grid(row=0, column=2, padx=10,
                             pady=5, ipadx=5, ipady=3)

        self.resetbtn = Button(self.btnfrm, text="Reset", bd=4,
                               relief=GROOVE, width=13, height=1, command=reset)
        self.resetbtn.grid(row=0, column=3, padx=10, pady=5, ipadx=5, ipady=3)

if __name__ == "__main__":
    main()