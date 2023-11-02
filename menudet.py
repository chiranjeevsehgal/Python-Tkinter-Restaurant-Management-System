from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import tkinter.font as tkFont
import pymysql

def main():
    root = Tk()
    app = MenuPage(root)
    root.mainloop()

class MenuPage():
    def __init__(self, root):

        # SOME IMPORTANT FUNCTIONS ------------------------------------------
        
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
        self.titleheadinglbl = Label(self.root, text=f"{appname} - Menu",
                                     bg="lightgrey", relief=GROOVE, font="calibri 11 bold")
        self.titleheadinglbl.pack(fill=X, side=TOP)

        self.contentfrm = Frame(self.root, bd=3, bg="lightgrey", relief=GROOVE)
        self.contentfrm.place(x=230, y=70, width=822, height=530)

        self.contentheadlbl = Label(self.contentfrm, text="Menu", bg="lightgrey",
                                    bd=3, relief=GROOVE, width=101, font="sans-serif 10 bold", anchor=CENTER)
        self.contentheadlbl.grid(row=0, column=0, columnspan=1)

        # VARIABLES-----------------------------------------------

        itemidinp = StringVar()
        fooditeminp = StringVar()
        priceinp = StringVar()
        typeinp = StringVar()
        codeinp = StringVar()

        # DETAIL FRAME, LABEL AND ENTRY BOXES-----------------------------------

        self.menudetailfrm = Frame(
            self.contentfrm, bg="lightgrey", relief=GROOVE)
        self.menudetailfrm.place(x=42, y=350)

        self.itemidlbl = Label(
            self.menudetailfrm, text="Item Id", bg="lightgrey")
        self.itemidlbl.grid(row=0, column=0, padx=15, pady=10)
        self.itemident = Entry(self.menudetailfrm, bd=3,
                               relief=GROOVE, textvariable=itemidinp)
        self.itemident.grid(row=0, column=1, ipadx=8, ipady=2)

        self.fooditemlbl = Label(
            self.menudetailfrm, text="Food Item", bg="lightgrey")
        self.fooditemlbl.grid(row=0, column=2, padx=15, pady=10)
        self.fooditement = Entry(
            self.menudetailfrm, bd=3, relief=GROOVE, textvariable=fooditeminp)
        self.fooditement.grid(row=0, column=3, ipadx=8, ipady=2)

        self.pricenumlbl = Label(
            self.menudetailfrm, text="Price", bg="lightgrey")
        self.pricenumlbl.grid(row=0, column=4, padx=15, pady=10)
        self.pricenument = Entry(
            self.menudetailfrm, bd=3, relief=GROOVE, textvariable=priceinp)
        self.pricenument.grid(row=0, column=5, ipadx=8, ipady=2)

        self.typelbl = Label(self.menudetailfrm,
                             text="Veg/Non-Veg", bg="lightgrey")
        self.typelbl.grid(row=1, column=0, padx=15, pady=10)
        self.typeent = Entry(self.menudetailfrm, bd=3,
                             relief=GROOVE, textvariable=typeinp)
        self.typeent.grid(row=1, column=1, ipadx=8, ipady=2)

        self.itemcodelbl = Label(
            self.menudetailfrm, text="Item Code", bg="lightgrey")
        self.itemcodelbl.grid(row=1, column=2, padx=15, pady=10)
        self.itemcodeent = Entry(
            self.menudetailfrm, bd=3, relief=GROOVE, textvariable=codeinp)
        self.itemcodeent.grid(row=1, column=3, ipadx=8, ipady=2)

        # FUNCTIONS-------------------------------------------------------------


        def exitmenu():
            # To exit the menu
            root.destroy()

        def fetch_data():
            # TO FETCH MENU DATA FROM THE DATABASE
            self.cont = []
            connect2db()
            self.curs.execute("SELECT * FROM menudetails")
            rows = self.curs.fetchall()
            if len(rows) != 0:
                self.menudatabase.delete(*self.menudatabase.get_children())
                for row in rows:
                    self.menudatabase.insert("", END, values=row)
                self.mydb.commit()
            self.mydb.close()

        def getdetails(event):
            # TO UPDATE THE ENTRY BOXES WITH DATABASE DATA
            
            row = self.menudatabase.focus()
            content = self.menudatabase.item(row)
            self.cont = content['values']
            self.itemident.config(state=DISABLED)
            itemidinp.set(self.cont[0])
            fooditeminp.set(self.cont[1])
            priceinp.set(self.cont[2])
            typeinp.set(self.cont[3])
            codeinp.set(self.cont[4])

        def addfooditem():
            #TO ADD NEW FOOD OPTION TO THE DATABASE

            exists = False
            if itemidinp.get() and fooditeminp.get() and priceinp.get() and typeinp.get() and codeinp.get():
                connect2db()
                self.curs.execute(f"SELECT * FROM `menudetails` WHERE `ItemId` = {itemidinp.get()}")
                enddb()
                tempdata = self.curs.fetchall()
                if len(tempdata) != 0:
                    exists = True

                if len(codeinp.get()) == 8:
                    if not exists:
                        try:
                            connect2db()
                            self.curs.execute("INSERT INTO menudetails VALUES(%s,%s,%s,%s,%s)", (itemidinp.get(), fooditeminp.get(), priceinp.get(), typeinp.get(), codeinp.get()))
                            enddb()
                            fetch_data()
                            clearinp()
                            messagebox.showinfo(
                                "Success", "Data has been successfully added.", parent=self.root)
                            
                        except Exception as e:
                            print(e)
                            messagebox.showerror(
                                "Connection Error!", "Data could not be added, Please try again later.", parent=self.root)
                    else:
                        messagebox.showerror(
                    "Error!", "Item already exists in the database.", parent=self.root)
                else:
                    messagebox.showerror(
                        "Error!", "Item code should be of eight characters.", parent=self.root)
            else:
                messagebox.showerror(
                    "Error!", "Please fill in the required information.", parent=self.root)

        def deletefooditem():
            # FUNCTION TO DELETE THE FOOD OPTION FROM THE DATABASE
            if itemidinp.get() and fooditeminp.get() and priceinp.get() and typeinp.get() and codeinp.get():
                try:
                    connect2db()
                    self.curs.execute(
                        "DELETE FROM menudetails WHERE ItemId = %s", (itemidinp.get()))
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
            itemidinp.set("")
            fooditeminp.set("")
            self.itemident.config(state=NORMAL)
            priceinp.set("")
            typeinp.set("")
            codeinp.set("")

        def edititem():
            # TO UPDATE ANY ENTRY IN THE DATABASE
            if itemidinp.get() and fooditeminp.get() and priceinp.get() and typeinp.get() and codeinp.get():
                if len(codeinp.get()) == 8:
                    try:
                        # Next line so that it is updated only if row is selected
                        if self.cont:
                            connect2db()
                            self.curs.execute("Update `menudetails` set `ItemName`=%s,`Price`=%s,`Veg/NonVeg`=%s,`ItemCode`=%s WHERE `ItemId` = %s",
                                        (fooditeminp.get(), priceinp.get(), typeinp.get(), codeinp.get(), itemidinp.get()))

                            enddb()
                            fetch_data()
                            clearinp()
                            messagebox.showinfo(
                                "Success", "Data has been successfully updated.", parent=self.root)

                        else:
                            messagebox.showerror(
                            "Error!", "Item does not exist in the database, Please add the item first.", parent=self.root)   
                        
                    except Exception as e:
                        messagebox.showerror(
                            "Error!", "Data could not be updated, Please try again later.", parent=self.root)
                else:
                    messagebox.showerror(
                        "Error!", "Item code should be of eight characters.", parent=self.root)
            
            elif not itemidinp.get() or not fooditeminp.get() or not priceinp.get() or not typeinp.get() or not codeinp.get():
                messagebox.showerror(
                    "Error!", "Please fill in the required information.", parent=self.root)
            
            else:
                messagebox.showerror(
                    "Error!", "Please select the entry to be updated.", parent=self.root)

        # MENU Buttons--------------------------------------------------------------

        self.menubtnfrm = Frame(self.contentfrm, bg="lightgrey", relief=GROOVE)
        self.menubtnfrm.place(x=62, y=470)

        self.addfooditembtn = Button(self.menubtnfrm, text="Add New Item",
                                     bd=2, bg="lightgrey", relief=GROOVE, command=addfooditem, width=15)
        self.addfooditembtn.grid(row=0, column=0, padx=10)

        self.editbtn = Button(self.menubtnfrm, text="Update Item", bd=2,
                              bg="lightgrey", relief=GROOVE, command=edititem, width=15)
        self.editbtn.grid(row=0, column=1, padx=10)

        self.deletefooditembtn = Button(self.menubtnfrm, text="Delete Item",
                                        bd=2, bg="lightgrey", relief=GROOVE, command=deletefooditem, width=15)
        self.deletefooditembtn.grid(row=0, column=2, padx=10)

        self.clearbtn = Button(self.menubtnfrm, text="Clear", bd=2,
                               bg="lightgrey", relief=GROOVE, command=clearinp, width=15)
        self.clearbtn.grid(row=0, column=3, padx=10)

        self.exitmenubtn = Button(self.menubtnfrm, text="Exit", bd=2,
                                  bg="lightgrey", relief=GROOVE, command=exitmenu, width=15)
        self.exitmenubtn.grid(row=0, column=4, padx=10)

        # MENU Treeview-------------------------------------------------------

        self.databasefrm = Frame(
            self.contentfrm, bg="lightgrey", bd=5, relief=GROOVE, width=686, height=400)
        self.databasefrm.place(x=0, y=25, width=815)

        self.xscrlbar = Scrollbar(self.databasefrm, orient=HORIZONTAL)
        self.yscrlbar = Scrollbar(self.databasefrm, orient=VERTICAL)
        self.xscrlbar.pack(side=BOTTOM, fill=X)
        self.yscrlbar.pack(side=RIGHT, fill=Y)

        self.menudatabase = ttk.Treeview(
            self.databasefrm, height=12, xscrollcommand=self.xscrlbar.set, yscrollcommand=self.yscrlbar.set)
        self.menudatabase['columns'] = (
            'Item Id', 'Food Item', 'Price', 'Veg/Non-Veg', 'Item Code')

        self.menudatabase.heading("Item Id", text="Item Id")
        self.menudatabase.heading("Food Item", text="Food Item")
        self.menudatabase.heading("Price", text="Price")
        self.menudatabase.heading("Veg/Non-Veg", text="Veg/Non-Veg")
        self.menudatabase.heading("Item Code", text="Item Code")

        self.menudatabase['show'] = 'headings'

        self.xscrlbar.config(command=self.menudatabase.xview)

        self.menudatabase.column("Item Id", width=100, anchor=CENTER)
        self.menudatabase.column("Food Item", width=140, anchor=CENTER)
        self.menudatabase.column("Price", width=140, anchor=CENTER)
        self.menudatabase.column("Veg/Non-Veg", width=140, anchor=CENTER)
        self.menudatabase.column("Item Code", width=120, anchor=CENTER)

        self.menudatabase.pack(fill=BOTH, expand=TRUE)
        fetch_data()
        self.menudatabase.bind("<ButtonRelease-1>", getdetails)

if __name__ == "__main__":
    main()