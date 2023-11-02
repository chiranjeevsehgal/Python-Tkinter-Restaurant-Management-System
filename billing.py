from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import tkinter.font as tkFont
import win32api
import pymysql
import datetime
import random
import sys
import os

def main():
    root = Tk()
    app = BillingWindow(root)
    root.mainloop()

class BillingWindow():
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
        self.root.configure(background="ivory2")
        
        self.root.state('zoomed')

        self.root.maxsize(1300, 650)
        self.root.minsize(1300, 650)

        self.titlehead = Label(self.root, text=f"{appname} - Billing",
                               bg="lightgrey", relief=GROOVE, font="calibri 11 bold")
        self.titlehead.pack(fill=X, side=TOP)

    # FONTS------------------------------------------------------------------
        helv11 = tkFont.Font(family="Helvetica",size=11,weight="normal")
        helv10 = tkFont.Font(family="Helvetica",size=10,weight="normal")

# SECTION 1 BILLING -------------------------------------------------------------------------

    # VARIABLES--------------------------------------------------------

        billnum = StringVar()
        custnameinp = StringVar()
        custcontactinp = StringVar()
        datebill = StringVar()
        itempurchasedinp = StringVar()
        quantityinp = StringVar()
        costperiteminp = StringVar()

    # DETAILS FRAME, LABEL AND ENTRY------------------------------------

        self.detailfrm = Frame(self.root, bg="lightgrey", bd=3, relief=GROOVE)
        self.detailfrm.place(x=65, y=55, width=352, height=562)

        self.detaillbl = Label(self.detailfrm, text="Enter Details", bg="lightgrey",bd=4, relief=GROOVE, font="sans-serif 10 bold", width=42, height=1)
        self.detaillbl.grid(row=0, column=0, columnspan=2,pady=0, ipady=4, padx=0)

        self.billnumlbl = Label(
            self.detailfrm, text="Bill Number:", bg="lightgrey", bd=2, font="sans-serif 11")
        self.billnumlbl.grid(row=1, column=0, pady=10, padx=15)

        self.billnumentry = Entry(self.detailfrm, textvariable=billnum, bd=3, relief=GROOVE, state=DISABLED)
        self.billnumentry.grid(row=1, column=1, ipady=3, ipadx=10, pady=10)

        self.custnamelbl = Label(
            self.detailfrm, text="Name:", bg="lightgrey", bd=3, font="sans-serif 11")
        self.custnamelbl.grid(row=2, column=0, pady=9, padx=15)

        self.custnameentry = Entry(
            self.detailfrm, textvariable=custnameinp, bd=3, relief=GROOVE)
        self.custnameentry.grid(row=2, column=1, padx=20, ipady=3, ipadx=10, pady=9)

        self.custcontactlbl = Label(
            self.detailfrm, text="Contact:", bg="lightgrey",bd=3, font="sans-serif 11")
        self.custcontactlbl.grid(row=3, column=0, pady=9, padx=15)

        self.custcontactentry = Entry(
            self.detailfrm, textvariable=custcontactinp, bd=3, relief=GROOVE)
        self.custcontactentry.grid(row=3, column=1, padx=20, ipady=3, ipadx=10, pady=9)

        self.datelbl = Label(self.detailfrm, text="Date:", bg="lightgrey", bd=2, font="sans-serif 11")
        self.datelbl.grid(row=4, column=0, pady=9, padx=15)

        self.dateentry = Entry(self.detailfrm, textvariable=datebill, bd=3, relief=GROOVE, state=DISABLED)
        self.dateentry.grid(row=4, column=1, padx=20, ipady=3, ipadx=10, pady=9)

        self.itempurchasedlbl = Label(
            self.detailfrm, text="Item purchased:", bg="lightgrey", bd=2, font="sans-serif 11")
        self.itempurchasedlbl.grid(row=5, column=0, pady=9, padx=15)

        self.itempurchasedentry = Entry(self.detailfrm, textvariable=itempurchasedinp,
                                bd=3, relief=GROOVE, state=DISABLED)
        self.itempurchasedentry.grid(row=5, column=1, padx=20, ipady=3, ipadx=10, pady=9)

        self.quantitylbl = Label(
            self.detailfrm, text="Quantity:", bg="lightgrey", bd=2, font="sans-serif 11")
        self.quantitylbl.grid(row=6, column=0, pady=9, padx=15)

        self.quantityentry = Entry(self.detailfrm, textvariable=quantityinp, bd=3, relief=GROOVE, state=DISABLED)
        self.quantityentry.grid(row=6, column=1, padx=20, ipady=3, ipadx=10, pady=9)

        self.costperitemlbl = Label(
            self.detailfrm, text="Cost per unit:", bg="lightgrey", bd=2, font="sans-serif 11")
        self.costperitemlbl.grid(row=7, column=0, pady=9, padx=15)

        self.costperitementry = Entry(self.detailfrm, textvariable=costperiteminp, bd=3, relief=GROOVE, state=DISABLED)
        self.costperitementry.grid(row=7, column=1, padx=20, ipady=3, ipadx=10, pady=9)

    # FUNCTIONS----------------------------------------------------
        
           
        def newbill():
            # To reset and create a new bill
            self.count = 0
            try:
                self.count = 0
                connect2db()
                self.curs.execute(
                    "SELECT Keyvalue FROM `otherdetails` WHERE `id` LIKE 'billnumber'")
                number = self.curs.fetchall()
                if len(number) != 0:
                    billnumval = number[0][0]
                if billnumval != billnum:
                    billnum.set(billnumval)
                reset_details()
                self.newbtn.config(state=DISABLED)
                self.custnameentry.config(state=NORMAL)
                self.custcontactentry.config(state=NORMAL)
                date_billset()
                enddb()

            except Exception as e:
                messagebox.showerror(
                    "Error!", "Error in creating new bill!", parent=self.root)

        def bill_number():
            # To fetch bill number from the database
            try:
                connect2db()
                self.curs.execute(
                    "SELECT Keyvalue FROM `otherdetails` WHERE `id` LIKE 'billnumber'")
                number = self.curs.fetchall()
                if len(number) != 0:
                    billnumval = number[0][0]
                billnum.set(billnumval)

                enddb()

            except Exception as e:
                messagebox.showerror(
                    "Error!", "Not able to fetch, generating random bill no.!", parent=self.root)
                billnum.set(random.randint(3111, 9999))

        def date_billset():
            # To feed the date and time in the bill
            datebill.set(datetime.datetime.now().strftime(
                "%d/%m/%Y, %H:%M:%S"))
        
        bill_number()
        date_billset()
        self.grtotal = []

        def add_item():
            # To add an item to the bill receipt
            if itempurchasedinp.get() and quantityinp.get() and costperiteminp.get():
                self.count += 1
                quantint = int(quantityinp.get())
                costint = int(costperiteminp.get())
                totalamt = quantint * costint
                self.grtotal.append(totalamt)

                try:
                    connect2db()
                    self.curs.execute(
                        "SELECT `ItemCode` FROM `menudetails` WHERE `ItemName` = %s", (itempurchasedinp.get()))
                    content = self.curs.fetchall()
                    if len(content) != 0:
                        code_value = content[0][0]
                    else:
                        messagebox.showerror(
                            "Connection Error!", "Itemcode could not be fetched.", parent=self.root)
                    enddb()

                    self.addbtn.config(state=NORMAL)
                    self.itempurchasedentry.config(state=NORMAL)
                    self.clearbtn.config(state=NORMAL)

                except Exception as e:
                    messagebox.showerror(
                        "Error!", "Item could not be fetched from the database, Please try again later.", parent=self.root)

                if int(quantityinp.get()) < 10:

                    if costint >= 1 and costint <= 9:
                        if totalamt >=1 and totalamt<=9:
                            self.billtxt.insert(
                                END, f"\n{code_value}                     {quantityinp.get()}                      {costperiteminp.get()}                      {totalamt}")
                        else:
                            if totalamt >=10 and totalamt<=99:
                                self.billtxt.insert(
                                    END, f"\n{code_value}                     {quantityinp.get()}                     {costperiteminp.get()}                     {totalamt}")
                            else:
                                self.billtxt.insert(
                                    END, f"\n{code_value}                     {quantityinp.get()}                     {costperiteminp.get()}                    {totalamt}")
                                
                    if costint >= 10 and costint <= 99:
                        if totalamt >=10 and totalamt<=99:
                            self.billtxt.insert(
                                END, f"\n{code_value}                     {quantityinp.get()}                     {costperiteminp.get()}                     {totalamt}")
                        else:
                            self.billtxt.insert(
                                END, f"\n{code_value}                     {quantityinp.get()}                     {costperiteminp.get()}                    {totalamt}")

                    elif costint >= 100 and costint <= 999:
                        if totalamt >=100 and totalamt<=999:
                            self.billtxt.insert(
                                END, f"\n{code_value}                     {quantityinp.get()}                    {costperiteminp.get()}                    {totalamt}")
                        else:
                            self.billtxt.insert(
                                END, f"\n{code_value}                     {quantityinp.get()}                    {costperiteminp.get()}                   {totalamt}")
                        

                    elif costint >= 1000 and costint <= 9999:
                        if totalamt >=1000 and totalamt<=9999:
                            self.billtxt.insert(
                                END, f"\n{code_value}                     {quantityinp.get()}                   {costperiteminp.get()}                   {totalamt}")
                        else:
                            self.billtxt.insert(
                                END, f"\n{code_value}                     {quantityinp.get()}                   {costperiteminp.get()}                  {totalamt}")

                    elif costint >= 10000 and costint <= 99999:
                        if totalamt >=10000 and totalamt<=99999:
                            self.billtxt.insert(
                                END, f"\n{code_value}                     {quantityinp.get()}                  {costperiteminp.get()}                  {totalamt}")
                        else:
                            self.billtxt.insert(
                                END, f"\n{code_value}                     {quantityinp.get()}                  {costperiteminp.get()}                 {totalamt}")
                    
                    self.billtotalbtn.config(state=NORMAL)
                            
                else:
                    messagebox.showerror(
                        "Error!", "Quantity for an item should be less than 10.", parent=self.root)

            elif itempurchasedinp.get() and not quantityinp.get() and costperiteminp.get():
                messagebox.showerror(
                    "Error!", "Please enter the quantity.", parent=self.root)

            else:
                messagebox.showerror(
                    "Error!", "Please enter all the fields correctly.", parent=self.root)
            
        def fetchitemdetails():
            # To fetch the item detail from the database for the inputed item id
            purchased_code = itempurchasedinp.get()
            if itempurchasedinp.get():
                try:
                    connect2db()
                    self.curs.execute(
                        "SELECT `Price`, `ItemName`, `ItemCode` FROM `menudetails` WHERE `ItemId` = %s", (purchased_code))
                    content = self.curs.fetchall()

                    if len(content) != 0:
                        price_value = content[0][0]
                        name_value = content[0][1]
                        code_value = content[0][2]
                        costperiteminp.set(price_value)
                        itempurchasedinp.set(name_value)
                        self.fetchitembtn.config(state=DISABLED)
                    else:
                        messagebox.showerror(
                            "Error!", "Item not found in the database.", parent=self.root)
                    enddb()

                    self.addbtn.config(state=NORMAL)
                    self.itempurchasedentry.config(state=NORMAL)
                    self.clearbtn.config(state=NORMAL)

                except Exception as e:
                    messagebox.showerror(
                        "Error!", "Data could not be fetched from the database, Please try again later.", parent=self.root)
            else:
                messagebox.showerror(
                    "Error!", "Please enter the item id.", parent=self.root)

        def clear():
            # To clear the item fields
            itempurchasedinp.set("")
            quantityinp.set("")
            costperiteminp.set("")
            self.fetchitembtn.config(state=NORMAL)
            self.addbtn.config(state=DISABLED)
            self.savebtn.config(state=DISABLED)
            self.printbtn.config(state=DISABLED)
            self.billtotalbtn.config(state=DISABLED)
            total_toggle()

        def reset_details():
            # To clear and reset all the details and fields
            custnameinp.set("")
            custcontactinp.set("")
            itempurchasedinp.set("")
            quantityinp.set("")
            costperiteminp.set("")
            self.billtxt.delete(1.0, END)
            self.grtotal.clear()
            DefaultBill()
            date_billset()

            self.custnameentry.config(state=NORMAL)
            self.custcontactentry.config(state=NORMAL)
            self.billgenbtn.config(state=NORMAL)
            self.fetchitembtn.config(state=DISABLED)
            self.billtotalbtn.config(state=DISABLED)
            self.addbtn.config(state=DISABLED)
            self.savebtn.config(state=DISABLED)
            self.printbtn.config(state=DISABLED)
            self.itempurchasedentry.config(state=DISABLED)
            self.quantityentry.config(state=DISABLED)
            self.costperitementry.config(state=DISABLED)

        def verify_customer():
        # To verify the customer details
            if custnameinp.get() and custcontactinp.get():
                if len(custcontactinp.get()) == 10:

                    if custcontactinp.get().isnumeric():
                        return True
                    else:
                        messagebox.showerror(
                        "Error", "Please enter a valid mobile number.", parent=self.root)
                else:
                    messagebox.showerror(
                    "Error!", "Please enter a valid mobile number.", parent=self.root)

            elif custnameinp.get() and not custcontactinp.get():
                messagebox.showerror(
                    "Error!", "Please enter the customer's mobile number.", parent=self.root)
            
            elif not custnameinp.get() and custcontactinp.get():
                messagebox.showerror(
                    "Error!", "Please enter the customer's name.", parent=self.root)
            
            else:
                messagebox.showerror(
                    "Error!", "Please fill in the required customer information.", parent=self.root)

        def generate_bill():
                # To generate the basic bill format
                self.count = 0
                if verify_customer():

                    self.billtxt.insert(END, f"\nBill no. - {billnum.get()}")
                    self.billtxt.insert(
                        END, f"\nCustomer Name - {custnameinp.get()}")
                    self.billtxt.insert(
                        END, f"\nCustomer Contact - +91 {custcontactinp.get()}")
                    self.billtxt.insert(END, f"\nDate - {datebill.get()}")
                    self.billtxt.insert(
                        END, "\n================================================================================")
                    self.billtxt.insert(
                        END, "\nDescription              Quantity              Unit Price               Amount")
                    self.billtxt.insert(
                        END, "\n================================================================================")

                    self.custnameentry.config(state=DISABLED)
                    self.custcontactentry.config(state=DISABLED)
                    self.itempurchasedentry.config(state=NORMAL)
                    self.quantityentry.config(state=NORMAL)
                    self.costperitementry.config(state=NORMAL)
                    self.fetchitembtn.config(state=NORMAL)
                    self.billgenbtn.config(state=DISABLED)
                    self.grtotal.clear()

        def total_toggle():
            # To keep the total button enabled or disabled depending upon bill items
            if self.count>0:
                self.billtotalbtn.config(state=NORMAL)

        def total_bill():
            # To calculate and display the total bill
            self.displaytotalamt = 0
            if self.count > 0:
                for i in range(len(self.grtotal)):
                    self.displaytotalamt = self.displaytotalamt+self.grtotal[i]

                self.billtxt.insert(
                    END, "\n================================================================================")
                self.billtxt.insert(
                    END, f"\n                                               Total Amount = ₹{self.displaytotalamt}")
                self.billtxt.insert(
                    END, "\n================================================================================")
                self.savebtn.config(state=NORMAL)
                self.printbtn.config(state=NORMAL)
                self.billtotalbtn.config(state=DISABLED)
                self.fetchitembtn.config(state=DISABLED)
                self.addbtn.config(state=DISABLED)
                self.clearbtn.config(state=DISABLED)
            else:
                messagebox.showerror(
                    "Error!", "Please enter atleast one item.", parent=self.root)

        def save_bill():
            # To save the bill to the computer
            userchoice = messagebox.askyesno(
                "Confirm?", f"Do you want to save bill no. {billnum.get()}?", parent=self.root)
            if userchoice > 0:
                try:
                    self.bill_content = self.billtxt.get("1.0", END)
                    
                    
                    # To get the desktop location for bill
                    home_dir = os.path.expanduser("~")  # Get the home directory
                    desktop_dir = os.path.join(home_dir, "Desktop")  # Join the home directory path with "Desktop"
    
                    if os.path.isdir(desktop_dir):  # Check if the desktop directory exists
                        self.desktoploc = desktop_dir

                    isExist = os.path.exists(f"{self.desktoploc}/BillMor/Bills")
                    if not isExist:
                        os.makedirs(f"{self.desktoploc}/BillMor/Bills")
                        
                    myfile = open(f"{self.desktoploc}/BillMor/Bills/Bill "+str(billnum.get()) +
                                  " - "+custnameinp.get()+".txt", "w", encoding='utf-8')
                    myfile.write(self.bill_content)
                    myfile.close()
                    messagebox.showinfo(
                        "Success!", f"Bill No. {billnum.get()} has been saved.", parent=self.root)
                    self.newbtn.config(state=NORMAL)
                    self.resetdetailsbtn.config(state=DISABLED)
                    updatecustdetails()

                    if billnum.get():
                        try:
                            connect2db()
                            inc = int(billnum.get())+1
                            self.curs.execute(
                                "UPDATE `otherdetails` SET `Keyvalue` = '%s' WHERE `otherdetails`.`id` = 'billnumber'", (inc))

                            enddb()

                        except Exception as e:
                            messagebox.showerror(
                                "Error!", "Bill Number could not be updated to the database!", parent=self.root)

                except Exception as e:
                    messagebox.showerror(
                        "Error", f"Error saving bill no. {billnum.get()}")

        def print_bill():
            # To print the bill

            filename = "Bill "+str(billnum.get()) +" - "+custnameinp.get()+".txt"
            try:
                os.startfile(f"{self.desktoploc}/BillMor/Bills/{filename}", "print")
                if os.path.exists(filename):
                    os.remove(filename)
            except Exception as e:
                    messagebox.showerror(
                        "Error!", "Bill could not be printed.", parent=self.root)
                
        def updatecustdetails():
            # ''' To upload the customer details for a saved bill to the database
            
            try:
                connect2db()
                self.curs.execute("INSERT INTO customerdetails VALUES(NULL,%s,%s, %s,%s)", ( custnameinp.get(), custcontactinp.get(), datebill.get(), str(self.displaytotalamt)))
                enddb()
                
            except Exception as e:
                messagebox.showerror(
                    "Error!", "Customer details could not be updated to the database.", parent=self.root)
           
        def exit_billing():
            root.destroy()

    # BILLING SCREEN BUTTONS--------------------------------------

        self.btnfrm = Frame(self.detailfrm,
                            relief=GROOVE, bg="lightgrey")
        self.btnfrm.place(x=16, y=380, width=330, height=162)

        self.newbtn = Button(self.btnfrm, text="New Bill", bd=3, relief=GROOVE, width=12, command=newbill, state=DISABLED)
        self.newbtn.grid(row=0, column=0, padx=4, pady=5, ipady=2)

        self.clearbtn = Button(
            self.btnfrm, text="Clear", bd=3, relief=GROOVE, width=12, command=clear, state=DISABLED)
        self.clearbtn.grid(row=0, column=1, padx=4, pady=5, ipady=2)

        self.resetdetailsbtn = Button(
            self.btnfrm, text="Reset", bd=3, relief=GROOVE, width=12, command=reset_details)
        self.resetdetailsbtn.grid(row=0, column=2, padx=4, pady=5, ipady=2)

        self.billgenbtn = Button(self.btnfrm, text="Generate Bill", bd=3, relief=GROOVE, width=12, command=generate_bill)
        self.billgenbtn.grid(row=1, column=0, padx=4, pady=5, ipady=2)

        self.fetchitembtn = Button(self.btnfrm, text="Fetch Details", bd=3, relief=GROOVE, width=12, state=DISABLED, command=fetchitemdetails)
        self.fetchitembtn.grid(row=1, column=1, padx=4, pady=5, ipady=2)

        self.addbtn = Button(self.btnfrm, text="Add", bd=3, relief=GROOVE, width=12, state=DISABLED, command=add_item)
        self.addbtn.grid(row=1, column=2, padx=4, pady=5, ipady=2)

        self.billtotalbtn = Button(self.btnfrm, text="Total", bd=3, relief=GROOVE, width=12, state=DISABLED, command=total_bill)
        self.billtotalbtn.grid(row=2, column=0, padx=4, pady=5, ipady=2)

        self.savebtn = Button(self.btnfrm, text="Save Bill", bd=3, relief=GROOVE, width=12, state=DISABLED, command=save_bill)
        self.savebtn.grid(row=2, column=1, padx=4, pady=5, ipady=2)

        self.printbtn = Button(self.btnfrm, text="Print Bill", bd=3, relief=GROOVE, width=12, state=DISABLED, command=print_bill)
        self.printbtn.grid(row=2, column=2, padx=4, pady=5, ipady=2)

        self.exitbtn = Button(self.btnfrm, text="Exit", bd=3, relief=GROOVE, width=12, state=NORMAL, command=exit_billing)
        self.exitbtn.grid(row=3, column=1, padx=0, pady=5, ipady=2, columnspan=1)

# SECTION 2 CALCULATOR ------------------------------------------------------------------------

    # CALCULATOR FRAME------------------------------------------------------------

        self.calcfrm = Frame(
            self.root, bg="lightgrey", bd=3, relief=GROOVE)
        self.calcfrm.place(x=545, y=57, height=286, width=310)

    # CALCULATOR FUNCTIONS----------------------------------------------------------

        def entry(event):
            # To define some special entries in the calculator
            txt = event.widget.cget('text')
            if txt == '=':
                if inpvar.get().isdigit():
                    value = int(inpvar.get())
                else:
                    try:
                        value = eval(inpvar.get())
                    except Exception as e:
                        value = "ERROR"
                inpvar.set(value)
                self.inp.update()
            elif txt == "C":
                inpvar.set("")
            else:
                inpvar.set(inpvar.get()+txt)
                self.inp.update()

    # CALCULATOR WIDGETS-------------------------------------------------------------

        inpvar = StringVar()
        inpvar.set("")
        self.inp = Entry(self.calcfrm, textvariable=inpvar, font=helv10,width=42, bg="lightgrey", bd=4, relief=GROOVE)
        self.inp.grid(row=0, column=0, columnspan=9, ipady=10, pady=2)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="7", height=2, width=8)
        self.btn.grid(row=1, column=0, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="8", height=2, width=8)
        self.btn.grid(row=1, column=1, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="9", height=2, width=8)
        self.btn.grid(row=1, column=2, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="+", height=2, width=8)
        self.btn.grid(row=1, column=3, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="4", height=2, width=8)
        self.btn.grid(row=2, column=0, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="5", height=2, width=8)
        self.btn.grid(row=2, column=1, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="6", height=2, width=8)
        self.btn.grid(row=2, column=2, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="-", height=2, width=8)
        self.btn.grid(row=2, column=3, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="1", height=2, width=8)
        self.btn.grid(row=3, column=0, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="2", height=2, width=8)
        self.btn.grid(row=3, column=1, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="3", height=2, width=8)
        self.btn.grid(row=3, column=2, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="*", height=2, width=8)
        self.btn.grid(row=3, column=3, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text=".", height=2, width=8)
        self.btn.grid(row=4, column=0, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="0", height=2, width=8)
        self.btn.grid(row=4, column=1, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="C", height=2, width=8)
        self.btn.grid(row=4, column=2, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)

        self.btn = Button(self.calcfrm, bd=5, relief=GROOVE,
                          text="=", height=2, width=8)
        self.btn.grid(row=4, column=3, padx=2, pady=5)
        self.btn.bind("<Button-1>", entry)


# SECTION 3 MENU TREEVIEW -----------------------------------------------------------------------
        
    # FUNCTIONS ---------------------------------------

        def fetch_data():
            # TO FETCH THE MENU DATA FROM THE DATABASE
            connect2db()
            self.curs.execute("SELECT `ItemId`, `ItemName`, `ItemCode` FROM `menudetails`")
            rows = self.curs.fetchall()
            if len(rows) != 0:
                self.menudatabase.delete(*self.menudatabase.get_children())
                for row in rows:
                    self.menudatabase.insert("", END, values=row)
                self.mydb.commit()
            self.mydb.close()

    # FRAMES AND HEADING --------------------------------
        
        self.menucontentfrm = Frame(self.root, bd=3, bg="lightgrey", relief=GROOVE)
        self.menucontentfrm.place(x=890, y=57, width=326, height=286)

        self.contentheadlbl = Label(self.menucontentfrm, text="Item Details", bg="lightgrey",
                                    bd=3, relief=GROOVE, width=39, font="sans-serif 10 bold", anchor=CENTER)
        self.contentheadlbl.grid(row=0, column=0, columnspan=1)

    # MAIN TREEVIEW--------------------------------
        self.databasefrm = Frame(
            self.menucontentfrm, bg="lightgrey", bd=5, relief=GROOVE, width=389, height=286)
        self.databasefrm.place(x=0, y=25, width=318)

        self.xscrlbar = Scrollbar(self.databasefrm, orient=HORIZONTAL)
        self.yscrlbar = Scrollbar(self.databasefrm, orient=VERTICAL)
        self.xscrlbar.pack(side=BOTTOM, fill=X)
        self.yscrlbar.pack(side=RIGHT, fill=Y)

        self.menudatabase = ttk.Treeview(
            self.databasefrm, height=10, xscrollcommand=self.xscrlbar.set, yscrollcommand=self.yscrlbar.set)
        self.menudatabase['columns'] = (
            'Item Id', 'Food Item', 'Item Code')

        self.menudatabase.heading("Item Id", text="Item Id")
        self.menudatabase.heading("Food Item", text="Food Item")
        self.menudatabase.heading("Item Code", text="Item Code")

        self.menudatabase['show'] = 'headings'

        self.xscrlbar.config(command=self.menudatabase.xview)

        self.menudatabase.column("Item Id", width=60, anchor=CENTER)
        self.menudatabase.column("Food Item", width=130, anchor=CENTER)
        self.menudatabase.column("Item Code", width=90, anchor=CENTER)

        self.menudatabase.pack(fill=BOTH, expand=TRUE)
        fetch_data()

# SECTION 4 RECEIPT AREA -----------------------------------------------------------------------

        self.billfrm = LabelFrame(
            self.root, text="Bill Area:", bd=3, bg="lightgrey", relief=GROOVE)
        self.billfrm.place(x=545, y=370, width=670, height=246)

        self.txtscrollbar = Scrollbar(self.billfrm)
        self.txtscrollbar.pack(side=RIGHT, fill=Y)
        self.billtxt = Text(self.billfrm, bg="white",
                            yscrollcommand=self.txtscrollbar)
        self.billtxt.pack(fill=BOTH, expand=TRUE)
        self.txtscrollbar.config(command=self.billtxt.yview)

        def DefaultBill():
            self.billtxt.insert(END, "\t\t\t           Cafe Serenade")
            self.billtxt.insert(
                END, "\n\t\t        123, Mall Avenue, Lucknow - 226001")
            self.billtxt.insert(END, "\n\t\t\t     Contact - +91 9876583491")
            self.billtxt.insert(
                END, "\n================================================================================")
            
        DefaultBill()

if __name__ == "__main__":
    main()