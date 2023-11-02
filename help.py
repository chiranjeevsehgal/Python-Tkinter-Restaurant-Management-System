from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import tkinter.font as tkFont
import pymysql
import datetime
import smtplib
import ssl
from email.message import EmailMessage

def main():
    root = Tk()
    app = HelpEmailer(root)
    root.mainloop()

class HelpEmailer:

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
        self.title_lbl = Label(self.root, text=f"{appname} - Help",
                               bg="lightgrey", relief=GROOVE, font="calibri 12 bold")
        self.title_lbl.pack(fill=X, side=TOP)

        self.helpfrm = Frame(self.root, bg="lightgrey", bd=6, relief=GROOVE)
        self.helpfrm.place(x=315, y=120, width=653, height=350)

        self.logintitle = Label(self.helpfrm, text="Help", bg="lightgrey",
                                font="TimesNewRoman 11 bold", anchor=CENTER, bd=4, relief=GROOVE)
        self.logintitle.pack(fill=X, side=TOP)

        self.entryfrm = LabelFrame(
            self.helpfrm, text="Enter Details:", bd=4, bg="lightgrey", font="sans-serif 10")
        self.entryfrm.place(x=0, y=33, height=306, width=640)

        # FONTS------------------------------------------------------------------
        helv11 = tkFont.Font(family="Helvetica", size=11, weight="normal")
        helv10 = tkFont.Font(family="Helvetica", size=10, weight="normal")

        # VARIABLES-------------------------------------------------------------

        probleminp = StringVar()
        descriptioninp = StringVar()
        filterinp = StringVar()

        # USERNAME PASSWORD FRAME, LABEL AND ENTRY---------------------------------

        self.helpdetfrm = Frame(self.entryfrm, bg="lightgrey", relief=GROOVE)
        self.helpdetfrm.place(x=20, y=27)

        self.searchlbl = Label(
            self.helpdetfrm, text="Type:", bg="lightgrey", font=helv11)
        self.searchlbl.grid(row=0, column=0, padx=15, pady=15)

        self.filterbox = ttk.Combobox(
            self.helpdetfrm, state="readonly", width=22, textvariable=filterinp)
        self.filterbox['values'] = (
            "Select", "Add/Delete Login", "Technical Assistance", "Maintenance", "Demo")
        self.filterbox.grid(row=0, column=1, ipadx=8, ipady=4)
        self.filterbox.current(0)

        self.problbl = Label(
            self.helpdetfrm, text="Subject:", bg="lightgrey", font=helv11)
        self.problbl.grid(row=1, column=0, padx=15, pady=14)

        self.probentry = Entry(
            self.helpdetfrm, textvariable=probleminp, bd=3, relief=GROOVE, font=helv10)
        self.probentry.grid(row=1, column=1, ipadx=10, ipady=3)

        self.desclbl = Label(
            self.helpdetfrm, text="Description:", bg="lightgrey", font=helv11)
        self.desclbl.grid(row=2, column=0, padx=15, pady=14)

        self.descentry = Entry(
            self.helpdetfrm, textvariable=descriptioninp, bd=3, relief=GROOVE, font=helv10)
        self.descentry.grid(row=2, column=1, ipadx=10, ipady=3)

        # FUNCTIONS---------------------------------------------------------

        def emailbodycontent():
            # Body content for the email
            typevar = filterinp.get()
            contvar = f"""Dear User, 
Your complaint for the {typevar} has been successfully registered.
Our team will get in touch with you soon!
We regret the inconvenience caused and appreciate your patience and cooperation.
            """
            return contvar

        def emailsubjectcontent():
            # Subject content for the email/
            typevar = filterinp.get()
            subjvar = f"Reply: {typevar} complaint!"
            return subjvar

        def fetchreceiveremail():
            # To fetch the reciever email id from the database
            connect2db()
            self.curs.execute(
                "SELECT Keyvalue FROM `otherdetails` WHERE `id` LIKE 'receiveremail'")
            secdata = self.curs.fetchall()
            enddb()
            if len(secdata) != 0:
                rec_email = secdata[0][0]
            return rec_email

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

        def updatecompttodb():
            # TO ADD THE COMPLAINT TO THE DATABASE
            date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            try:
                connect2db()
                self.curs.execute("INSERT INTO complaintdetails VALUES(NULL,%s,%s,%s,%s)", (
                    filterinp.get(), probleminp.get(), descriptioninp.get(), date))
                enddb()

            except Exception as e:
                messagebox.showerror(
                    "Error!", "Complaint could not be updated to the database.", parent=self.root)

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

        def sendemailfunc():
            # To send the email
            # Sender email id
            email_sender = fetchsenderemail()
            # App password created after 2 step verification
            email_password = fetchemailpassword()
            # Receiver email id
            email_receiver = fetchreceiveremail()

            subject = emailsubjectcontent()
            body = emailbodycontent()
            try:
                if probleminp.get() and descriptioninp.get():
                    if filterinp.get() != "Select":
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
                            smtp.quit()
                        messagebox.showinfo(
                            "Success", "Your complaint has been successfully registered.", parent=self.root)
                        updatecompttodb()
                        reset()
                    else:
                        messagebox.showerror(
                            "Error!", "Please select the complaint type.", parent=self.root)

                else:
                    messagebox.showerror(
                        "Error!", "Please fill in the required information.", parent=self.root)

            except Exception as e:
                messagebox.showerror(
                    "Error!", "Complaint could not be registered, Please try again later.", parent=self.root)

        def reset():
            # To reset the fields
            self.filterbox.current(0)
            probleminp.set("")
            descriptioninp.set("")

        def exitfunc():
            # To exit
            root.destroy()

        # SIGNUP BUTTONS AND FRAME--------------------------------------

        self.btnfrm = Frame(self.entryfrm, bg="lightgrey", relief=GROOVE)
        self.btnfrm.place(x=100, y=204)

        self.complainbtn = Button(self.btnfrm, text="Complain", bd=4,
                                   relief=GROOVE, width=13, height=1, command=sendemailfunc)
        self.complainbtn.grid(row=0, column=1, padx=10,
                               pady=5, ipadx=5, ipady=3)

        self.exitbtn = Button(self.btnfrm, text="Exit", bd=4, relief=GROOVE,
                              width=13, height=1, state=NORMAL, command=exitfunc)
        self.exitbtn.grid(row=0, column=2, padx=10, pady=5, ipadx=5, ipady=3)

        self.resetbtn = Button(self.btnfrm, text="Reset", bd=4,
                               relief=GROOVE, width=13, height=1, command=reset)
        self.resetbtn.grid(row=0, column=3, padx=10, pady=5, ipadx=5, ipady=3)

if __name__ == "__main__":
    main()