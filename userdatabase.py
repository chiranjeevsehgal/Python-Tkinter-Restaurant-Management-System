from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import pymysql

def main():
    root = Tk()
    app = UseridDB(root)
    root.mainloop()

class UseridDB():
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
        self.titleheadinglbl = Label(self.root, text=f"{appname} - User Database",
                                     bg="lightgrey", relief=GROOVE, font="calibri 11 bold")
        self.titleheadinglbl.pack(fill=X, side=TOP)

        self.contentfrm = Frame(self.root, bd=3, bg="lightgrey", relief=GROOVE)
        self.contentfrm.place(x=281, y=70, width=726, height=530)

        self.contentheadlbl = Label(self.contentfrm, text="User Id Database", bg="lightgrey",
                                    bd=3, relief=GROOVE, width=89, font="sans-serif 10 bold", anchor=CENTER)
        self.contentheadlbl.grid(row=0, column=0, columnspan=1)
        
        # FUNCTIONS-------------------------------------------------------------
        
        def exituserdb():
            # To exit a window
            root.destroy()

        def fetch_data():
            # TO FETCH LOGIN USER DATA FROM THE DATABASE 
            connect2db()
            self.curs.execute("SELECT * FROM logindetails")
            rows = self.curs.fetchall()
            if len(rows) != 0:
                self.useriddatabase.delete(*self.useriddatabase.get_children())
                for row in rows:
                    self.useriddatabase.insert("", END, values=row)
                self.mydb.commit()
            self.mydb.close()
    
        # Buttons--------------------------------------------------------------

        self.userdbfrm = Frame(self.contentfrm, bg="lightgrey", relief=GROOVE)
        self.userdbfrm.place(x=99, y=470)

        self.exituserdbbtn = Button(self.userdbfrm, text="Exit", bd=2,
                                  bg="lightgrey", relief=GROOVE, command=exituserdb, width=15)
        self.exituserdbbtn.grid(row=0, column=1, padx=200)

        # Treeview-------------------------------------------------------

        self.databasefrm = Frame(
            self.contentfrm, bg="lightgrey", bd=5, relief=GROOVE, width=486, height=675)
        self.databasefrm.place(x=0, y=25, width=720)

        self.xscrlbar = Scrollbar(self.databasefrm, orient=HORIZONTAL)
        self.yscrlbar = Scrollbar(self.databasefrm, orient=VERTICAL)
        self.xscrlbar.pack(side=BOTTOM, fill=X)
        self.yscrlbar.pack(side=RIGHT, fill=Y)

        self.useriddatabase = ttk.Treeview(
            self.databasefrm, height=18, xscrollcommand=self.xscrlbar.set, yscrollcommand=self.yscrlbar.set)
        self.useriddatabase['columns'] = (
            'Sr No.', 'Name', 'Contact', 'Username')

        self.useriddatabase.heading("Sr No.", text="Sr No.")
        self.useriddatabase.heading("Name", text="Name")
        self.useriddatabase.heading("Contact", text="Contact")
        self.useriddatabase.heading("Username", text="Username")

        self.useriddatabase['show'] = 'headings'

        self.xscrlbar.config(command=self.useriddatabase.xview)

        self.useriddatabase.column("Sr No.", width=70, anchor=CENTER)
        self.useriddatabase.column("Name", width=110, anchor=CENTER)
        self.useriddatabase.column("Contact", width=110, anchor=CENTER)
        self.useriddatabase.column("Username", width=110, anchor=CENTER)

        self.useriddatabase.pack(fill=BOTH, expand=TRUE)
        fetch_data()

if __name__ == "__main__":
    main()