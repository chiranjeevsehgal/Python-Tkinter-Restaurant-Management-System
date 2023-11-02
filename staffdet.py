from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import pymysql

def main():
    root = Tk()
    app = Staff(root)
    root.mainloop()

class Staff():

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
        self.root.title(appname)

        self.root.state('zoomed')

        self.root.maxsize(1300, 650)
        self.root.minsize(1300, 650)

        self.root.configure(background="ivory2")
        self.titleheadinglbl = Label(self.root, text=f"{appname} - Staff Details",
                                     bg="lightgrey", relief=GROOVE, font="calibri 11 bold")
        self.titleheadinglbl.pack(fill=X, side=TOP)

        self.contentfrm = Frame(self.root, bd=3, bg="lightgrey", relief=GROOVE)
        self.contentfrm.place(x=230, y=70, width=822, height=510)

        self.contentheadlbl = Label(self.contentfrm, text="Staff Details", bg="lightgrey",
                                    bd=3, relief=GROOVE, width=101, font="sans-serif 10 bold", anchor=CENTER)
        self.contentheadlbl.grid(row=0, column=0, columnspan=1)

        # VARIABLES-----------------------------------------------

        nameinp = StringVar()
        phoneinp = StringVar()
        salaryinp = StringVar()
        empidinp = StringVar()
        aadharinp = StringVar()
        addressinp = StringVar()

        # DETAIL FRAME, LABEL AND ENTRY BOXES-----------------------------------

        self.staffdetailfrm = Frame(
            self.contentfrm, bg="lightgrey", relief=GROOVE)
        self.staffdetailfrm.place(x=45, y=340)
        self.empidlbl = Label(self.staffdetailfrm,
                              text="Emp Id.", bg="lightgrey")
        self.empidlbl.grid(row=0, column=0, padx=15, pady=10)
        self.empident = Entry(self.staffdetailfrm, bd=3,
                              relief=GROOVE, textvariable=empidinp)
        self.empident.grid(row=0, column=1, ipadx=8, ipady=2)

        self.namelbl = Label(self.staffdetailfrm, text="Name", bg="lightgrey")
        self.namelbl.grid(row=0, column=2, padx=15, pady=10)
        self.nameent = Entry(self.staffdetailfrm, bd=3,
                             relief=GROOVE, textvariable=nameinp)
        self.nameent.grid(row=0, column=3, ipadx=8, ipady=2)

        self.phonenumlbl = Label(
            self.staffdetailfrm, text="Phone No.", bg="lightgrey")
        self.phonenumlbl.grid(row=0, column=4, padx=15, pady=10)
        self.phonenument = Entry(
            self.staffdetailfrm, bd=3, relief=GROOVE, textvariable=phoneinp)
        self.phonenument.grid(row=0, column=5, ipadx=8, ipady=2)

        self.salarylbl = Label(
            self.staffdetailfrm, text="Salary", bg="lightgrey")
        self.salarylbl.grid(row=1, column=0, padx=15, pady=10)
        self.salaryent = Entry(
            self.staffdetailfrm, bd=3, relief=GROOVE, textvariable=salaryinp)
        self.salaryent.grid(row=1, column=1, ipadx=8, ipady=2)

        self.aadharlbl = Label(self.staffdetailfrm,
                               text="Aadhar No.", bg="lightgrey")
        self.aadharlbl.grid(row=1, column=2, padx=15, pady=10)
        self.aadharent = Entry(self.staffdetailfrm, bd=3,
                               relief=GROOVE, textvariable=aadharinp)
        self.aadharent.grid(row=1, column=3, ipadx=8, ipady=2)

        self.addresslbl = Label(self.staffdetailfrm,
                                text="Address", bg="lightgrey")
        self.addresslbl.grid(row=1, column=4, padx=15, pady=10)
        self.addressent = Entry(self.staffdetailfrm,
                                bd=3, relief=GROOVE, textvariable=addressinp)
        self.addressent.grid(row=1, column=5, ipadx=8, ipady=2)

        # FUNCTIONS----------------------------------------

        def exitstaffwindow():
            # To exit the window
            root.destroy()

        def fetch_data():
            # TO FETCH STAFF DATA FROM THE DATABASE
            self.cont = []
            connect2db()
            self.curs.execute(
                "SELECT * FROM `staffdetails` ORDER BY `EmployeeId` ASC")
            rows = self.curs.fetchall()

            if len(rows) != 0:
                self.staffdatabase.delete(*self.staffdatabase.get_children())
                for row in rows:
                    self.staffdatabase.insert("", END, values=row)
                self.mydb.commit()
            self.mydb.close()

        def getdetails(event):
            # TO UPDATE THE ENTRY BOXES WITH DATABASE DATA
            row = self.staffdatabase.focus()
            content = self.staffdatabase.item(row)
            self.cont = content['values']
            empidinp.set(self.cont[0])
            nameinp.set(self.cont[1])
            self.empident.config(state=DISABLED)
            phoneinp.set(self.cont[2])
            salaryinp.set(self.cont[3])
            aadharinp.set(self.cont[4])
            addressinp.set(self.cont[5])

        def addstaffwindow():
            # TO ADD NEW DATA TO THE DATABASE
            exists = False
            if empidinp.get() and nameinp.get() and phoneinp.get() and salaryinp.get() and aadharinp.get() and addressinp.get():
                connect2db()
                self.curs.execute("SELECT * FROM `staffdetails` WHERE `EmployeeId` LIKE %s", {empidinp.get()})
                tempdata = self.curs.fetchall()
                enddb()
                if len(tempdata) != 0:
                    exists = True
                
                if not exists:
                    try:
                        connect2db()
                        self.curs.execute("INSERT INTO staffdetails VALUES(%s,%s,%s, %s,%s,%s)", (empidinp.get(
                        ), nameinp.get(), phoneinp.get(), salaryinp.get(), aadharinp.get(), addressinp.get()))
                        enddb()
                        fetch_data()
                        clearinp()
                        messagebox.showinfo(
                            "Success", "Data has been successfully added.", parent=self.root)
                    except Exception as e:
                        messagebox.showerror(
                            "Connection Error!", "Data could not be added, Please try again later.", parent=self.root)
                else:
                    messagebox.showerror(
                    "Error!", "Entry already exists in the database.", parent=self.root)
            else:
                messagebox.showerror(
                    "Error!", "Please fill in the required information.", parent=self.root)

        def deletestaffwindow():
            # TO DELETE THE DATA FROM DATABASE
            if nameinp.get() and phoneinp.get() and salaryinp.get() and empidinp.get() and aadharinp.get() and addressinp.get():
                try:
                    connect2db()
                    self.curs.execute(
                        "DELETE FROM staffdetails WHERE EmployeeId = %s", (empidinp.get()))
                    enddb()
                    fetch_data()
                    clearinp()
                    messagebox.showinfo(
                        "Success!", "Data has been successfully deleted.", parent=self.root)
                except Exception as e:
                    messagebox.showerror(
                        "Connection Error!", "Data could not be deleted, Please try again later.", parent=self.root)

            else:
                messagebox.showerror(
                    "Error!", "Please select the entry to be deleted.", parent=self.root)

        def clearinp():
            # TO CLEAR THE ENTRY BOXES
            self.cont = []
            empidinp.set("")
            nameinp.set("")
            phoneinp.set("")
            self.empident.config(state=NORMAL)
            salaryinp.set("")
            aadharinp.set("")
            addressinp.set("")

        def editstaffdetails():
            # TO UPDATE AN ENTRY IN THE DATABASE
            if empidinp.get() and nameinp.get() and phoneinp.get() and salaryinp.get() and aadharinp.get() and addressinp.get():
                try:
                    # Next line so that it is updated only if row is selected
                    if self.cont:
                        connect2db()
                        self.curs.execute("Update staffdetails set Name=%s,MobileNumber=%s, Salary=%s, Aadhar=%s, Address=%s WHERE EmployeeId = %s", (
                            nameinp.get(), phoneinp.get(), salaryinp.get(), aadharinp.get(), addressinp.get(), empidinp.get()))
                        enddb()
                        fetch_data()
                        clearinp()
                        messagebox.showinfo(
                            "Success", "Data has been successfully updated.", parent=self.root)
                    
                    else:
                            messagebox.showerror(
                            "Error!", "Item does not exist in the database, Please add the item first.", parent=self.root)  

                except Exception as e:
                    print(e)
                    messagebox.showerror(
                        "Error!", "Data could not be updated, Please try again later.", parent=self.root)
                    
            elif not empidinp.get() or not nameinp.get() or not phoneinp.get() or not salaryinp.get() or not aadharinp.get() or not addressinp.get():
                messagebox.showerror(
                    "Error!", "Please fill in the required information.", parent=self.root)

            else:
                messagebox.showerror(
                    "Error!", "Please select the entry to be updated.", parent=self.root)

        # STAFF Buttons------------------------------------------------------------

        self.staffbtnfrm = Frame(
            self.contentfrm, bg="lightgrey", relief=GROOVE)
        self.staffbtnfrm.place(x=48, y=450)

        self.addstaffbtn = Button(self.staffbtnfrm, text="Add Staff", bd=2,
                                  bg="lightgrey", relief=GROOVE, command=addstaffwindow, width=16, )
        self.addstaffbtn.grid(row=0, column=0,padx=10)

        self.editstaffbtn = Button(self.staffbtnfrm, text="Update Details", bd=2,
                                   bg="lightgrey", relief=GROOVE, command=editstaffdetails, width=16, )
        self.editstaffbtn.grid(row=0, column=1,padx=10)

        self.deletestaffbtn = Button(self.staffbtnfrm, text="Delete Staff", bd=2,
                                     bg="lightgrey", relief=GROOVE, command=deletestaffwindow, width=16, )
        self.deletestaffbtn.grid(row=0, column=2,padx=10)

        self.clearbtn = Button(self.staffbtnfrm, text="Clear", bd=2,
                               bg="lightgrey", relief=GROOVE, command=clearinp, width=16, )
        self.clearbtn.grid(row=0, column=3,padx=10)

        self.exitstaffbtn = Button(self.staffbtnfrm, text="Exit", bd=2,
                                   bg="lightgrey", relief=GROOVE, command=exitstaffwindow, width=16, )
        self.exitstaffbtn.grid(row=0, column=4,padx=10)

        # STAFF TreeView------------------------------------------------------------

        self.databasefrm = Frame(
            self.contentfrm, bg="lightgrey", bd=5, relief=GROOVE, width=686, height=400)
        self.databasefrm.place(x=0, y=25, width=815)

        self.xscrlbar = Scrollbar(self.databasefrm, orient=HORIZONTAL)
        self.yscrlbar = Scrollbar(self.databasefrm, orient=VERTICAL)
        self.xscrlbar.pack(side=BOTTOM, fill=X)
        self.yscrlbar.pack(side=RIGHT, fill=Y)

        self.staffdatabase = ttk.Treeview(
            self.databasefrm, height=12, xscrollcommand=self.xscrlbar.set, yscrollcommand=self.yscrlbar.set)

        self.staffdatabase['columns'] = (
            'Employee Id', 'Name', 'Mobile Number', 'Salary', 'Aadhar Number', 'Address')

        self.staffdatabase.heading("Employee Id", text="Employee Id")
        self.staffdatabase.heading("Name", text="Name")
        self.staffdatabase.heading("Mobile Number", text="Mobile Number")
        self.staffdatabase.heading("Salary", text="Salary")
        self.staffdatabase.heading("Aadhar Number", text="Aadhar Number")
        self.staffdatabase.heading("Address", text="Address")

        self.staffdatabase['show'] = 'headings'

        self.xscrlbar.config(command=self.staffdatabase.xview)

        self.staffdatabase.column("Employee Id", width=102, anchor=CENTER)
        self.staffdatabase.column("Name", width=120)
        self.staffdatabase.column("Mobile Number", width=122)
        self.staffdatabase.column("Salary", width=122)
        self.staffdatabase.column("Aadhar Number", width=120)
        self.staffdatabase.column("Address", width=150)

        self.staffdatabase.pack(fill=BOTH, expand=TRUE)
        fetch_data()
        self.staffdatabase.bind("<ButtonRelease-1>", getdetails)

if __name__ == "__main__":
    main()