from tkinter import *
from tkinter import messagebox
import datetime
import random
import sys

def main():
    root=Tk()
    app = LoginPage(root)
    root.mainloop()



class LoginPage:
    
    def __init__(self,root):
        self.root = root
        self.root.geometry("800x500")
        self.root.maxsize(800,500)
        self.root.minsize(800,500)
        self.root.title("Restaurant Management System")
        self.root.configure(background="ivory2")
        self.title_lbl = Label(self.root, text="Restaurant Management System", bg="lightgrey", relief=GROOVE,font="calibri 15 bold")
        self.title_lbl.pack(fill=X, side=TOP)

        self.loginfrm = Frame(self.root,bg="lightgrey", bd=6,relief=GROOVE)
        # self.loginfrm = Frame(self.root,bg="lightgrey", bd=6,relief=GROOVE,width=50,height=500)
        # self.loginfrm.pack(fill=X,expand=1,padx=200,ipady=100)
        self.loginfrm.place(x=200,y=100,width=400,height=300)

        self.logintitle = Label(self.loginfrm, text="Login", bg="lightgrey", font = "TimesNewRoman 15 bold",anchor=CENTER , bd=4, relief=GROOVE)
        self.logintitle.pack(fill=X,side=TOP)

        self.entryfrm = LabelFrame(self.loginfrm, text="Enter Details:", bd = 4, bg="lightgrey",font="sans-serif 10")
        self.entryfrm.pack(fill=BOTH,expand=TRUE)

        self.usernamelbl = Label(self.entryfrm, text="Username:",bg="lightgrey")
        self.usernamelbl.grid(row=0,column=0,pady=10,padx=5)
        self.passwordlbl = Label(self.entryfrm, text="Password:",bg="lightgrey")
        self.passwordlbl.grid(row=1,column=0,pady=10,padx=5)

        # -----------------------VARIABLES------------------------------

        username = StringVar()
        password = StringVar()

        # --------------------------------------------------------------

        self.usernameentry = Entry(self.entryfrm, textvariable=username,bd=3, relief=GROOVE)
        self.usernameentry.grid(row=0,column=1,padx=5)
        self.passwordentry = Entry(self.entryfrm, textvariable=password,bd=3, relief=GROOVE,show="*")
        self.passwordentry.grid(row=1,column=1,padx=5)

        # -----------------------FUNCTIONS------------------------------
        def exitlogin():
            root.destroy()
        
        def checklogin():
            myuserid = "admin"
            mypassword = "admin"
            if username.get() == myuserid and password.get() == mypassword:
                self.billingbtn.config(state=NORMAL)
                self.loginbtn.config(text="Exit", command=exitlogin)
            elif username.get() == "" or password.get() == "":
                messagebox.showerror("Empty!", "Please enter the details.",parent=self.root)
            else:
                messagebox.showinfo("Invalid!", "Invalid Credentials.",parent=self.root)

        def reset():
            username.set("")
            password.set("")

        def billing_section():
            self.newwindow = Toplevel(self.root)
            self.app = BillingWindow(self.newwindow)

        def staff_list():
            self.newwindow=Toplevel(self.root)
            self.app = Staff(self.newwindow)
            

        def helpfunc():
            messagebox.showinfo("Help", "You can contact us at _____@gmail.com", parent = self.root)

        def menuopen():
            self.newwindow= Toplevel(self.root)
            self.app= MenuPage(self.newwindow)

        # --------------------------------------------------------------

        self.btnfrm= Frame(self.entryfrm, bg="lightgrey",relief=GROOVE)
        self.btnfrm.place(x=21,y=93)
        
        self.loginbtn= Button(self.btnfrm, text="Log In", bd=4, relief=GROOVE,width=10,height=1,command=checklogin)
        self.loginbtn.grid(row=0, column=1,padx=10,pady=5,ipadx=5,ipady=3)

        self.billingbtn= Button(self.btnfrm, text="Billing", bd=4, relief=GROOVE,width=10,height=1,
        state=DISABLED, command=billing_section)
        self.billingbtn.grid(row=0,column=2,padx=10,pady=5,ipadx=5,ipady=3)
        
        self.resetbtn= Button(self.btnfrm, text="Reset", bd=4, relief=GROOVE,width=10,height=1,command=reset)
        self.resetbtn.grid(row=0, column=3,padx=10,pady=5,ipadx=5,ipady=3)

        self.menubtn= Button(self.btnfrm, text="Menu", bd=4, relief=GROOVE,width=10,height=1, command=menuopen)
        self.menubtn.grid(row=1, column=1,padx=10,pady=5,ipadx=5,ipady=3)

        self.staffbtn= Button(self.btnfrm, text="Staff Details", bd=4, relief=GROOVE,width=10,height=1,command=staff_list)
        self.staffbtn.grid(row=1, column=2,padx=10,pady=5,ipadx=5,ipady=3)

        self.helpbtn= Button(self.btnfrm, text="Help", bd=4, relief=GROOVE,width=10,height=1,command=helpfunc)
        self.helpbtn.grid(row=1, column=3,padx=10,pady=5,ipadx=5,ipady=3)

        # ----------------------------------------FOOTER-----------------------------------------
        self.footer_lbl = Label(self.root, text="CHIRANJEEV SEHGAL ©", bg="lightgrey", relief=GROOVE,font="calibri 8 bold")
        self.footer_lbl.pack(fill=X, side=BOTTOM)
        # ---------------------------------------------------------------------------------------


        
class BillingWindow():
        def __init__(self,root):
            self.root=root
            self.root.title("Billing")
            self.root.configure(background="ivory2")
            self.root.geometry("800x500")
            self.root.maxsize(800,500)
            self.root.minsize(800,500)
            self.titlehead= Label(self.root, text="Restaurant Management System", bg="lightgrey", relief=GROOVE,font="calibri 15 bold")
            self.titlehead.pack(fill=X, side=TOP)

            # -----------------------------DETAILS SECTION-------------------------------

            self.detailfrm = Frame(self.root, bg="lightgrey")
            self.detailfrm.place(x=30,y=55,width=295,height=405)

            self.detaillbl= Label(self.detailfrm, text="Enter Details", bg="lightgrey", bd=2, relief=GROOVE, font="sans-serif 10 bold",width=36)
            self.detaillbl.grid(row=0,column=0,columnspan=10)

            self.billnumlbl=Label(self.detailfrm, text="Bill Number:",bg="lightgrey", bd=2,font="sans-serif 10")
            self.billnumlbl.grid(row=2,column=0,pady=8,padx=10)
            self.custnamelbl=Label(self.detailfrm, text="Name:",bg="lightgrey", bd=2,font="sans-serif 10")
            self.custnamelbl.grid(row=3,column=0,pady=8,padx=10)
            self.custcontactlbl=Label(self.detailfrm, text="Contact:",bg="lightgrey", bd=2,font="sans-serif 10")
            self.custcontactlbl.grid(row=4,column=0,pady=8,padx=10)
            self.datelbl=Label(self.detailfrm, text="Date:",bg="lightgrey", bd=2,font="sans-serif 10")
            self.datelbl.grid(row=5,column=0,pady=8,padx=10)
            self.itempurchasedlbl=Label(self.detailfrm, text="Item purchased:",bg="lightgrey", bd=2,font="sans-serif 10")
            self.itempurchasedlbl.grid(row=6,column=0,pady=8,padx=10)
            self.quantitylbl=Label(self.detailfrm, text="Quantity:",bg="lightgrey", bd=2,font="sans-serif 10")
            self.quantitylbl.grid(row=7,column=0,pady=8,padx=10)
            self.costperitemlbl=Label(self.detailfrm, text="Cost per unit:",bg="lightgrey", bd=2,font="sans-serif 10")
            self.costperitemlbl.grid(row=8,column=0,pady=8,padx=10)

            

            # -----------------------VARIABLES------------------------------

            billnum = StringVar()
            custnameinp = StringVar()
            custcontactinp = StringVar()
            datebill = StringVar()
            itempurchasedinp = StringVar()
            quantityinp = StringVar()
            costperiteminp = StringVar()

            # --------------------------------------------------------------

            self.billnumentry=Entry(self.detailfrm,bg="lightgrey",textvariable=billnum, bd=2, relief=GROOVE,state=DISABLED,disabledbackground="lightgrey")
            self.billnumentry.grid(row=2,column=1,padx=20,pady=8)
            self.custnameentry=Entry(self.detailfrm,textvariable=custnameinp,bg="lightgrey", bd=2,relief=GROOVE)
            self.custnameentry.grid(row=3,column=1,padx=20,pady=8)
            self.custcontactentry=Entry(self.detailfrm,textvariable=custcontactinp,bg="lightgrey", bd=2,relief=GROOVE)
            self.custcontactentry.grid(row=4,column=1,padx=20,pady=8)
            self.dateentry=Entry(self.detailfrm,textvariable=datebill,bg="lightgrey", bd=2,relief=GROOVE,state=DISABLED,disabledbackground="lightgrey")
            self.dateentry.grid(row=5,column=1,padx=20,pady=8)
            self.itempurchasedentry=Entry(self.detailfrm,textvariable=itempurchasedinp, bg="lightgrey", bd=2,relief=GROOVE,state=DISABLED,disabledbackground="lightgrey")
            self.itempurchasedentry.grid(row=6,column=1,padx=20,pady=8)
            self.quantityentry=Entry(self.detailfrm,textvariable=quantityinp,bg="lightgrey", bd=2,relief=GROOVE,state=DISABLED,disabledbackground="lightgrey")
            self.quantityentry.grid(row=7,column=1,padx=20,pady=8)
            self.costperitementry=Entry(self.detailfrm, textvariable=costperiteminp,bg="lightgrey", bd=2,relief=GROOVE,state=DISABLED,disabledbackground="lightgrey")
            self.costperitementry.grid(row=8,column=1,padx=20,pady=8)

            # -----------------------FUNCTIONS------------------------------
            def bill_number():
                billnum.set(random.randint(3111,9999))
            def date_billset():
                datebill.set(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
            bill_number()
            date_billset()
            self.grtotal = []

            def add_item():
                if itempurchasedinp.get() and quantityinp.get() and costperiteminp.get():
                    self.count+=1
                    quantint = int(quantityinp.get())
                    costint = int(costperiteminp.get())
                    totalamt = quantint * costint
                    self.grtotal.append(totalamt)

                    if len(itempurchasedinp.get()) < 8:
                        temp = 8 - len(itempurchasedinp.get())
                        itempurchasedinp.set(itempurchasedinp.get()+" "*temp)

                        if costint >= 10 and costint <=99:
                            self.billtxt.insert(END, f"\n{itempurchasedinp.get()}          {quantityinp.get()}         {costperiteminp.get()}         {totalamt}")
                            
                        elif costint >= 100 and costint <=999:
                            self.billtxt.insert(END, f"\n{itempurchasedinp.get()}          {quantityinp.get()}         {costperiteminp.get()}        {totalamt}")
                        elif costint >= 1000 and costint <=9999:
                            self.billtxt.insert(END, f"\n{itempurchasedinp.get()}          {quantityinp.get()}         {costperiteminp.get()}       {totalamt}")

                    else:
                        if costint >= 1 and costint <=9:
                            self.billtxt.insert(END, f"\n{itempurchasedinp.get()}          {quantityinp.get()}         {costperiteminp.get()}          {totalamt}")
                        if costint >= 10 and costint <=99:
                            self.billtxt.insert(END, f"\n{itempurchasedinp.get()}          {quantityinp.get()}         {costperiteminp.get()}         {totalamt}")
                            
                        elif costint >= 100 and costint <=999:
                            self.billtxt.insert(END, f"\n{itempurchasedinp.get()}          {quantityinp.get()}         {costperiteminp.get()}        {totalamt}")
                        elif costint >= 1000 and costint <=9999:
                            self.billtxt.insert(END, f"\n{itempurchasedinp.get()}          {quantityinp.get()}         {costperiteminp.get()}       {totalamt}")
                        elif costint >= 10000 and costint <=99999:
                            self.billtxt.insert(END, f"\n{itempurchasedinp.get()}          {quantityinp.get()}         {costperiteminp.get()}      {totalamt}")
                else:
                    messagebox.showerror("Error!", "Please enter all the fields correctly.", parent=self.root)

            def clear():
                itempurchasedinp.set("")
                quantityinp.set("")
                costperiteminp.set("")
                
            def reset_details():
                custnameinp.set("")
                custcontactinp.set("")
                self.billtxt.delete(1.0,END)
                self.grtotal.clear()
                DefaultBill()

                self.billtotalbtn.config(state=DISABLED)
                self.addbtn.config(state=DISABLED)
                self.savebtn.config(state=DISABLED)
                self.itempurchasedentry.config(state=DISABLED)
                self.quantityentry.config(state=DISABLED)
                self.costperitementry.config(state=DISABLED)

            def generate_bill():
                self.count = 0
                if custnameinp.get() and custcontactinp.get():
                    self.billtxt.insert(END, f"\nBill no. - {billnum.get()}")
                    self.billtxt.insert(END, f"\nCustomer Name - {custnameinp.get()}")
                    self.billtxt.insert(END, f"\nCustomer Contact - +91 {custcontactinp.get()}")
                    self.billtxt.insert(END, f"\nDate - {datebill.get()}")
                    self.billtxt.insert(END, "\n==============================================")
                    self.billtxt.insert(END, "\nDescription   Quantity   Unit Price   Amount")
                    self.billtxt.insert(END, "\n==============================================")
                    self.billtotalbtn.config(state=NORMAL)
                    self.addbtn.config(state=NORMAL)
                    self.itempurchasedentry.config(state=NORMAL)
                    self.quantityentry.config(state=NORMAL)
                    self.costperitementry.config(state=NORMAL)
                    self.grtotal.clear()
                else:
                    messagebox.showinfo("Error", "Please enter the details.",parent=self.root)
               
            def total_bill():
                displaytotalamt = 0
                if self.count > 0:
                    for i in range(len(self.grtotal)):
                        displaytotalamt = displaytotalamt+self.grtotal[i]

                    self.billtxt.insert(END, "\n==============================================")
                    self.billtxt.insert(END, f"\n                        Total Amount = ₹{displaytotalamt}")
                    self.billtxt.insert(END, "\n==============================================")
                    self.savebtn.config(state=NORMAL)
                else:
                    messagebox.showerror("Error!", "Please enter atleast one item.",parent=self.root)


            def save_bill():
                userchoice = messagebox.askyesno("Confirm?", f"Do you want to save bill no. {billnum.get()}?",parent=self.root)
                if userchoice > 0:
                    try:
                        self.bill_content = self.billtxt.get("1.0",END)
                        myfile = open(f"{sys.path[0]}/Bill "+str(billnum.get())+"- "+custnameinp.get()+".txt", "w",encoding='utf-8')
                        myfile.write(self.bill_content)
                        myfile.close()
                        messagebox.showinfo("Success!", f"Bill No. {billnum.get()} has been saved.",parent=self.root)
                    except Exception as c:
                        messagebox.showerror("Error", f"Error saving bill no. {billnum.get()}")

            # --------------------------------------------------------------
            self.btnfrm = Frame(self.detailfrm,bd=2, relief=GROOVE, bg="lightgrey",)
            self.btnfrm.place(x=10,y=304,width=275,height=77)
            self.addbtn = Button(self.btnfrm,text="Add",bg="lightgrey",bd=2,relief=GROOVE,width=10,state=DISABLED,command=add_item)
            self.addbtn.grid(row=0, column=0,padx=5,pady=5)
            self.clearbtn = Button(self.btnfrm,text="Clear",bg="lightgrey",bd=2,relief=GROOVE,width=10,command=clear)
            self.clearbtn.grid(row=0, column=1,padx=5,pady=5)
            self.resetdetailsbtn = Button(self.btnfrm,text="Reset",bg="lightgrey",bd=2,relief=GROOVE,width=10,command=reset_details)
            self.resetdetailsbtn.grid(row=0, column=2,padx=5,pady=5)
            self.billgenbtn = Button(self.btnfrm,text="Generate Bill",bg="lightgrey",bd=2,relief=GROOVE,width=10,command=generate_bill)
            self.billgenbtn.grid(row=1, column=0,padx=5,pady=5)
            self.billtotalbtn = Button(self.btnfrm,text="Total",bg="lightgrey",bd=2,relief=GROOVE,width=10,state=DISABLED,command=total_bill)
            self.billtotalbtn.grid(row=1, column=1,padx=5,pady=5)
            self.savebtn = Button(self.btnfrm,text="Save Bill",bg="lightgrey",bd=2,relief=GROOVE,width=10,state=DISABLED,command=save_bill)
            self.savebtn.grid(row=1, column=2,padx=5,pady=5)

            # ---------------------------------------------------------------------------
            # ---------------------------CALCULATOR SECTION------------------------------

            self.calcfrm = Frame(self.root, bg="lightgrey", bd=3, relief=GROOVE)
            self.calcfrm.place(x=370, y=55,height=190,width=400)

            # ---------------------------CALCULATOR FUNCTION------------------------------

            def entry(event):
                txt = event.widget.cget('text')
                if txt == '=':
                    if inpvar.get().isdigit():
                        value = int(inpvar.get())
                    else:
                        try:
                            value = eval(inpvar.get())
                        except Exception as e:
                            print(e)
                            value= "ERROR"
                            # messagebox.showinfo("Error", "Bad Expression.")
                    inpvar.set(value)
                    self.inp.update()
                elif txt == "C":
                    inpvar.set("")
                else:
                    inpvar.set(inpvar.get()+txt)
                    self.inp.update()

            # ----------------------------------------------------------------------------
            # ---------------------------CALCULATOR WIDGETS------------------------------

            inpvar = StringVar()
            inpvar.set("")
            self.inp = Entry(self.calcfrm, textvariable=inpvar, font="lucida 10",width=55,bg="lightgrey", bd=3, relief=GROOVE)
            self.inp.grid(row=0, column=0, columnspan=4,ipady=5)

            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="7", height=1, width=10)
            self.btn.grid(row=1, column=0,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)
            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="8", height=1, width=10)
            self.btn.grid(row=1, column=1,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)
            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="9", height=1, width=10)
            self.btn.grid(row=1, column=2,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)
            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="+", height=1, width=10)
            self.btn.grid(row=1, column=3,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)

            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="4", height=1, width=10)
            self.btn.grid(row=2, column=0,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)
            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="5", height=1, width=10)
            self.btn.grid(row=2, column=1,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)
            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="6", height=1, width=10)
            self.btn.grid(row=2, column=2,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)
            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="-", height=1, width=10)
            self.btn.grid(row=2, column=3,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)

            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="1", height=1, width=10)
            self.btn.grid(row=3, column=0,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)
            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="2", height=1, width=10)
            self.btn.grid(row=3, column=1,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)
            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="3", height=1, width=10)
            self.btn.grid(row=3, column=2,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)
            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="*", height=1, width=10)
            self.btn.grid(row=3, column=3,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)

            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text=".", height=1, width=10)
            self.btn.grid(row=4, column=0,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)
            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="0", height=1, width=10)
            self.btn.grid(row=4, column=1,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)
            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="C", height=1, width=10)
            self.btn.grid(row=4, column=2,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)
            self.btn = Button(self.calcfrm,bd=5,relief=GROOVE, text="=", height=1, width=10)
            self.btn.grid(row=4, column=3,padx=2,pady=2)
            self.btn.bind("<Button-1>", entry)

            # ---------------------------------------------------------------------------
            # --------------------------------BILL AREA----------------------------------

            self.billfrm = LabelFrame(self.root,text="Bill Area:", bd=3, bg="lightgrey", relief=GROOVE)
            self.billfrm.place(x=370,y=260, width=400, height=200)

            self.txtscrollbar = Scrollbar(self.billfrm)
            self.txtscrollbar.pack(side=RIGHT, fill=Y)
            self.billtxt = Text(self.billfrm, bg="white",yscrollcommand=self.txtscrollbar)
            self.billtxt.pack(fill=BOTH, expand=TRUE)
            self.txtscrollbar.config(command=self.billtxt.yview)
            def DefaultBill():
                self.billtxt.insert(END, "\t       Restaurant Name")
                self.billtxt.insert(END, "\n\t123, Mall Avenue, Lucknow - 226001")
                self.billtxt.insert(END, "\n\t     Contact - +91 1234567890")
                self.billtxt.insert(END, "\n==============================================")
            DefaultBill()
            # ---------------------------------------------------------------------------

            # ---------------------------------------------------------------------------



class Staff():
    def __init__(self,root):
        self.root = root
        self.root.title("Staff Details:")
        self.root.geometry("600x500")
        self.root.configure(background="ivory2")
        self.titleheadinglbl= Label(self.root, text="Restaurant Management System", bg="lightgrey", relief=GROOVE,font="calibri 15 bold")
        self.titleheadinglbl.pack(fill=X,side=TOP)

        self.contentfrm = Frame(self.root, bd=3, bg="lightgrey", relief=GROOVE)
        self.contentfrm.place(x=90, y=100, width=399,height=300)

        self.contentheadlbl = Label(self.contentfrm, text="Staff Details-", bg="lightgrey", bd=3, relief=GROOVE, width=48,font="sans-serif 10", anchor="nw")
        self.contentheadlbl.grid(row=0, column=0,columnspan=10)

        # -----------------------STAFF LIST CONTENT----------------------------

        namelst = ["Ajay", "Amit", "Rahul", "Karan", "Rohit"]

        for item in range(len(namelst)):
            self.srnumlbl = Label(self.contentfrm,text=f"{item+1}-", bd=3, bg="lightgrey",width=5)
            self.srnumlbl.grid(row=item+1 , column=0)

        for item in range(len(namelst)):
            self.namelbl = Label(self.contentfrm,text=namelst[item], bd=3, bg="lightgrey",width=5)
            self.namelbl.grid(row=item+1 , column=1)

        for item in range(len(namelst)):
            self.phonenum = Label(self.contentfrm,text=f"+91 {random.randrange(8123456789,9999999999)}", bd=3, bg="lightgrey",width=12)
            self.phonenum.grid(row=item+1 , column=2)

        for item1 in range(len(namelst)):
            self.employeeid = Label(self.contentfrm,text=f"{random.randrange(12453,29675)}", bd=3, bg="lightgrey",width=6)
            self.employeeid.grid(row=item1+1 , column=3)
        
        def exitstaffwindow():
            root.destroy()

        self.exitstaffbtn = Button(self.root, text="Exit", bd=4, bg="lightgrey", relief=GROOVE,command=exitstaffwindow)
        self.exitstaffbtn.place(x=250,y=425,width=70)

        # ---------------------------------------------------------------------


class MenuPage():
    def __init__(self,root):
        self.root = root
        self.root.title("Menu:")
        self.root.geometry("600x500")
        self.root.maxsize(600,500)
        self.root.minsize(600,500)
        self.root.configure(background="ivory2")
        self.titleheadinglbl= Label(self.root, text="Restaurant Management System", bg="lightgrey", relief=GROOVE,font="calibri 15 bold")
        self.titleheadinglbl.pack(fill=X,side=TOP)

        self.contentfrm = Frame(self.root, bd=3, bg="lightgrey", relief=GROOVE)
        self.contentfrm.place(x=90, y=100, width=399,height=300)

        self.contentheadlbl = Label(self.contentfrm, text="Items we offer-", bg="lightgrey", bd=3, relief=GROOVE, width=48,font="sans-serif 10", anchor="nw")
        self.contentheadlbl.grid(row=0, column=0,columnspan=10)

        # -----------------------MENU CONTENT----------------------------
        foodlst = ["dosa", "pizza", "biryani", "samosa", "burger"]
        foodprc = ["70", "60", "110", "30", "44"]
        for item in range(len(foodlst)):
            self.srnumlbl = Label(self.contentfrm,text=f"{item+1}-", bd=3, bg="lightgrey",width=5)
            self.srnumlbl.grid(row=item+1 , column=0)

        for item in range(len(foodlst)):
            self.fooditm = Label(self.contentfrm,text=foodlst[item], bd=3, bg="lightgrey",width=30)
            self.fooditm.grid(row=item+1 , column=1)

        for item1 in range(len(foodprc)):
            self.foodprclbl = Label(self.contentfrm,text=f"₹ {foodprc[item1]}", bd=3, bg="lightgrey",width=10)
            self.foodprclbl.grid(row=item1+1 , column=2)
        
        def exitwindow():
            root.destroy()

        self.exitbtn = Button(self.root, text="Exit", bd=4, relief=GROOVE, bg="lightgrey", command=exitwindow)
        self.exitbtn.place(x=250,y=425,width=70)
        # ---------------------------------------------------------------



if __name__=="__main__":
    main()
