from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import pymysql

def main():
    root = Tk()
    app = CustomerDB(root)
    root.mainloop()

class CustomerDB():
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

        self.titleheadinglbl = Label(self.root, text=f"{appname} - Customer Database",
                                     bg="lightgrey", relief=GROOVE, font="calibri 11 bold")
        self.titleheadinglbl.pack(fill=X, side=TOP)

        self.contentfrm = Frame(self.root, bd=3, bg="lightgrey", relief=GROOVE)
        self.contentfrm.place(x=230, y=70, width=822, height=530)

        self.contentheadlbl = Label(self.contentfrm, text="Customer Database", bg="lightgrey",
                                    bd=3, relief=GROOVE, width=101, font="sans-serif 10 bold", anchor=CENTER)
        self.contentheadlbl.grid(row=0, column=0, columnspan=1)
        
        # FUNCTIONS-------------------------------------------------------------
        

        def exitcustomerdb():
            # To exit
            root.destroy()

        def fetch_data():
            # To fetch the data from the database
            ''' FUNCTION TO FETCH Menu DATA FROM THE DATABASE  '''
            connect2db()
            self.curs.execute("SELECT * FROM customerdetails")
            rows = self.curs.fetchall()
            if len(rows) != 0:
                self.custdatabase.delete(*self.custdatabase.get_children())
                for row in rows:
                    self.custdatabase.insert("", END, values=row)
                self.mydb.commit()
            self.mydb.close()
    
        # MENU Buttons--------------------------------------------------------------

        self.custdbfrm = Frame(self.contentfrm, bg="lightgrey", relief=GROOVE)
        self.custdbfrm.place(x=62, y=470)

        self.exitcustdbbtn = Button(self.custdbfrm, text="Exit", bd=2,
                                  bg="lightgrey", relief=GROOVE, command=exitcustomerdb, width=15)
        self.exitcustdbbtn.grid(row=0, column=1, padx=290, columnspan=4)

        # MENU Treeview-------------------------------------------------------

        self.databasefrm = Frame(
            self.contentfrm, bg="lightgrey", bd=5, relief=GROOVE, width=686, height=675)
        self.databasefrm.place(x=0, y=25, width=815)

        self.xscrlbar = Scrollbar(self.databasefrm, orient=HORIZONTAL)
        self.yscrlbar = Scrollbar(self.databasefrm, orient=VERTICAL)
        self.xscrlbar.pack(side=BOTTOM, fill=X)
        self.yscrlbar.pack(side=RIGHT, fill=Y)

        self.custdatabase = ttk.Treeview(
            self.databasefrm, height=18, xscrollcommand=self.xscrlbar.set, yscrollcommand=self.yscrlbar.set)
        self.custdatabase['columns'] = (
            'Sr No.', 'Name', 'Contact', 'Date', 'Amount')

        self.custdatabase.heading("Sr No.", text="Sr No.")
        self.custdatabase.heading("Name", text="Name")
        self.custdatabase.heading("Contact", text="Contact")
        self.custdatabase.heading("Date", text="Date")
        self.custdatabase.heading("Amount", text="Amount")

        self.custdatabase['show'] = 'headings'

        self.xscrlbar.config(command=self.custdatabase.xview)

        self.custdatabase.column("Sr No.", width=100, anchor=CENTER)
        self.custdatabase.column("Name", width=140, anchor=CENTER)
        self.custdatabase.column("Contact", width=140, anchor=CENTER)
        self.custdatabase.column("Date", width=140, anchor=CENTER)
        self.custdatabase.column("Amount", width=120, anchor=CENTER)

        self.custdatabase.pack(fill=BOTH, expand=TRUE)
        fetch_data()

if __name__ == "__main__":
    main()