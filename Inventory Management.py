import mysql.connector
import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox
from PIL import ImageTk#python imaging library
from datetime import date,datetime
mydb=mysql.connector.connect (host="localhost",user="root", passwd="12345")
myc=mydb.cursor()
def createdatabase():
    myc.execute("create database if not exists inventory")
    myc.execute("use inventory")
def createtables():
    myc.execute("create table if not exists inventory (ItemNo int primary key,Name varchar(50),Quantity int,DOE date,TOE varchar(50));")
    myc.execute("create table if not exists login (Empno int primary key,password varchar(50),Name VARCHAR(50));")
    myc.execute("create table if not exists Employee (Empno int Primary key,password varchar(50),Name VARCHAR(50),Position varchar(50),Salary int,gmail varchar(50), MobileNo bigint);")
    myc.execute("truncate table login")
    insert()
def insert():
    myc.execute("Select * from Employee")
    k=myc.fetchall()
    if k==[]:
        myc.execute("INSERT INTO Employee VALUES (526485, 'Nikhil@1992', 'Nikhil Anto', 'Inventory Manager', 6500, 'nikhil1975@gmail.com', 9876543210)")
        myc.execute("INSERT INTO Employee VALUES (856936, 'Subash123', 'Subash Nair', 'Inventory Specialist', 6333, '1983subash@gmail.com', 8765432109)")
        myc.execute("INSERT INTO Employee VALUES (885326, 'Ramesh@1991', 'Ramesh Pisharody', 'Inventory Coordinator', 8000, 'pisharody84@gmail.com', 7654321098)")
        myc.execute("INSERT INTO Employee VALUES (452365, 'MaheshKumar@4385', 'Mahesh Kumar', 'Inventory Analyst', 7500, 'mkumar@gmail.com', 6543210987)")
        myc.execute("INSERT INTO Employee VALUES (854712, 'Sureshsudheesh', 'Suresh Sudheesh', 'Warehouse Manager', 8520, 'sureshsudheesh@gmail.com', 5432109876)")
        myc.execute("INSERT INTO Employee VALUES (245163, 'John.Durai', 'John Durai', 'Warehouse Supervisor', 15000, 'jd1974@gmail.com', 4321098765)")
        myc.execute("INSERT INTO Employee VALUES (124578, 'Divya.Shasha', 'Divya Shasha', 'Logistics Coordinator', 12000, 'dsvijay@gmail.com', 3210987654)")
        myc.execute("INSERT INTO Employee VALUES (123569, 'Vijay.kumar', 'Vijay Kumar', 'Inventory Control Specialist', 13000, 'vijayvk2274@gmail.com', 2109876543)")
        myc.execute("INSERT INTO Employee VALUES (325698, 'Steph.Roni', 'Stephen Ronald', 'Inventory Clerk', 12563, 'strono@gmail.com', 1098765432)")
        mydb.commit()
def browse(window):
    window.geometry("1600x900")
    window.title("Browse")
    window.iconbitmap("logo.ico")
    bg10=ImageTk.PhotoImage(file="menu.png")
    bglb10=tk. Label(window,image=bg10)
    bglb10.place(x=-25,y=-50,width=1600,height=900)
    def show(window):
        va97=g.get()
        myc.execute('select * from inventory where ItemNo={}'.format(va97))
        er=myc.fetchall()
        r=[]
        total_rows=5
        total_columns=2
        for lk in er:
            for kl in lk:
                r.append(kl)
        hg=[("Item No.",r[0]),("Name",r[1]),("Quantity",r[2]),("Last Updated Date",r[3]),("Last Updated Time",r[4])]
        frm_form9 = tk.Frame(relief=tk.SUNKEN, borderwidth=5)
        frm_form9.pack()
        frm_form9.place(x=500,y=232)
        for i0 in range(total_rows):
            for j0 in range(total_columns):
                if j0 ==0:
                    entry10= tk.Label(frm_form9,text=hg[i0][j0], width=20,bg='#081229',fg='White',font=('Times New Roman', 15, 'bold'))
                else:
                    entry10 = tk.Label(frm_form9,text=hg[i0][j0], width=40, fg='#081229',bg='White',font=('Times New Roman', 15, ''))
                entry10.grid(row=i0, column=j0)
    def chck():
        v=g.get()
        myc.execute('select itemNo from inventory')
        er=myc.fetchall()
        r=[]
        for lk in er:
            for kl in lk:
                r.append(int(kl))
        print(r)
        print(v)
        if v=='':
            pass
        elif int(v) not in r:
            messagebox.showerror("Error","item doesn't Exist")
        else:
            show(window)
    g=tk.Entry(master=window,width=50)
    g.place(x=900,y=165)
    menu(window)
    click_btns=ImageTk.PhotoImage(file="search.jpeg")
    buttons=tk.Button(window,image=click_btns,command=lambda:chck(),relief=tk.FLAT,font=("Times New Roman","20","bold"),fg="white",bg="#081229")
    buttons.place(x=1200,y=165)
    window.mainloop()
def storage(window):
    window.destroy()
    window=tk.Tk()
    window.geometry("1600x900")
    window.title("Storage")
    window.iconbitmap("logo.ico")
    bg10=ImageTk.PhotoImage(file="menu.png")
    bglb10=tk. Label(window,image=bg10)
    bglb10.place(x=-25,y=-50,width=1600,height=900)
    menu(window)
    myc.execute("Select Quantity from inventory")
    gj=[]
    lk2=myc.fetchall()
    for hj in lk2:
        for jh in hj:
            gj.append(jh)
    var1 = sum(gj)
    var1=(var1/500)*100
    var2=str(var1)+"%"
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("custom.Horizontal.TProgressbar", troughcolor='white', background='#081229', thickness=0)
    progress_var = tk.DoubleVar()
    progressbar = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate", variable=progress_var,style="custom.Horizontal.TProgressbar")
    progressbar.place(x=500,y=232)
    percent=tk.Label(window,text=var2,font=("Times New Roman","15","bold"),fg="#081229",bg="white")
    percent.place(x=500,y=250)
    progress_var.set(var1)
    window.mainloop()
def remove(window):
    def submit():
        var1=e1.get()
        myc.execute("Select ItemNo from inventory")
        gj=[]
        lk2=myc.fetchall()
        for hj in lk2:
            for jh in hj:
                gj.append(jh)
        if var1=='':
            messagebox.showerror("Error","ALL THE FIELDS ARE REQUIRED")
        else:
            try:
                var1=int(var1)
                print(gj)
                if var1 not in gj:
                    messagebox.showerror("Error","Item Doesn't Exisit")
                else:
                    myc.execute("Delete from inventory where ItemNo={}".format(var1))
                    mydb.commit()
                    messagebox.showinfo("Success","Product Removed Successfully")
                    window.destroy()
                    Home(window)
            except:
                mydb.rollback()
                messagebox.showerror("Error","Only Integers allowed")
    window.destroy()
    window=tk.Tk()
    window.geometry("1600x900")
    window.title("Remove")
    window.iconbitmap("logo.ico")
    bg10=ImageTk.PhotoImage(file="menu.png")
    bglb10=tk. Label(window,image=bg10)
    bglb10.place(x=-25,y=-50,width=1600,height=900)
    menu(window)
    frm_form9 = tk.Frame(bg="White",relief=tk.FLAT, borderwidth=0)
    frm_form9.pack()
    frm_form9.place(x=500,y=232)
    l1=tk.Label(frm_form9,text='Product ID.',bg='white',fg='#081229')
    l1.config(font=("Times New Roman","20","bold"))
    l1.grid(row=0,column=0)
    e1=tk.Entry(frm_form9,width=25,border=1)
    e1.config(font=("Times New Roman","15","bold"),bg='white',fg='#081229')
    e1.grid(row=0,column=1)
    button2=tk.Button(window,text="SUBMIT",command=lambda:submit(),font=("Times New Roman","15","bold"),fg="white",bg="#081229")
    button2.place(x=650,y=380)
    window.mainloop()
def update(window):
    def submit():
        var1=e1.get()
        var2=e2.get()
        myc.execute("Select ItemNo from inventory")
        gj=[]
        var4=date.today()
        var5=datetime.now().time()
        var6=var5.strftime('%H:%M:%S')
        lk2=myc.fetchall()
        for hj in lk2:
            for jh in hj:
                gj.append(jh)
        if var1=='' or var2=='':
            messagebox.showerror("Error","ALL THE FIELDS ARE REQUIRED")
        else:
            try:
                var1=int(var1)
                var2=int(var2)
                myc.execute("Select Quantity from inventory where ItemNo <> {}".format(var1))
                jk=[]
                lk=myc.fetchall()
                for hj in lk:
                    for jh in hj:
                        jk.append(jh)
                var3 = sum(jk)
                if var1 not in gj:
                    messagebox.showerror("Error","Item Doesn't Exisit")
                elif (var2+var3)>500:
                    messagebox.showerror("Error","Insufficient Storage")
                else:
                    myc.execute("Update inventory set quantity={} where ItemNo={}".format(var2,var1))
                    myc.execute("Update inventory set DOE='{}' where ItemNo={}".format(var4,var1))
                    myc.execute("Update inventory set TOE='{}' where ItemNo={}".format(var6,var1))
                    mydb.commit()
                    messagebox.showinfo("Success","Product Updated Successfully")
                    window.destroy()
                    Home(window)
            except:
                mydb.rollback()
                messagebox.showerror("Error","Only Integers allowed")
    window.destroy()
    window=tk.Tk()
    window.geometry("1600x900")
    window.title("Update")
    window.iconbitmap("logo.ico")
    bg10=ImageTk.PhotoImage(file="menu.png")
    bglb10=tk. Label(window,image=bg10)
    bglb10.place(x=-25,y=-50,width=1600,height=900)
    menu(window)
    frm_form9 = tk.Frame(bg="White",relief=tk.FLAT, borderwidth=0)
    frm_form9.pack()
    frm_form9.place(x=500,y=232)
    l1=tk.Label(frm_form9,text='Product ID.',bg='white',fg='#081229')
    l1.config(font=("Times New Roman","20","bold"))
    l1.grid(row=0,column=0)
    e1=tk.Entry(frm_form9,width=25,border=1)
    e1.config(font=("Times New Roman","15","bold"),bg='white',fg='#081229')
    e1.grid(row=0,column=1)
    e2=tk.Entry(frm_form9,width=25,border=1)
    e2.config(font=("Times New Roman","15","bold"),bg='white',fg='#081229')
    e2.grid(row=1,column=1)
    l3=tk.Label(frm_form9,text='Quantity',bg='white',fg='#081229',font=("Times New Roman","20","bold"))
    l3.grid(row=1,column=0)
    button2=tk.Button(window,text="SUBMIT",command=lambda:submit(),font=("Times New Roman","15","bold"),fg="white",bg="#081229")
    button2.place(x=650,y=380)
    window.mainloop()
def add(window):
    def submit():
        var1=e1.get()
        var2=e2.get()
        var3=e3.get()
        var4=date.today()
        var5=datetime.now().time()
        var6=var5.strftime('%H:%M:%S')
        myc.execute("Select Name from inventory")
        gj=[]
        lk2=myc.fetchall()
        for hj in lk2:
            for jh in hj:
                gj.append(jh)
        myc.execute("Select Quantity from inventory")
        jk=[]
        lk=myc.fetchall()
        for hj in lk:
            for jh in hj:
                jk.append(jh)
        var7 = sum(jk)
        if var1=='' or var2=='' or var3=='':
            messagebox.showerror("Error","ALL THE FIELDS ARE REQUIRED")
        else:
            var2=var2.lower()
            try:
                if var2 in gj:
                    messagebox.showerror("Error","Item Already Exisits")
                elif (int(var3)+var7)>500:
                    messagebox.showerror("Error","Insufficient Storage")
                else:
                    var1=int(var1)
                    var3=int(var3)
                    myc.execute("INSERT INTO INVENTORY VALUES({},'{}',{},'{}','{}')".format(var1,var2,var3,var4,var6))
                    mydb.commit()
                    messagebox.showinfo("Success","Product Added Successfully")
                    window.destroy()
                    Home(window)
            except:
                mydb.rollback()
                messagebox.showerror("Error","Only Integers allowed for ProductID and Quantity")
    window.destroy()
    window=tk.Tk()
    window.geometry("1600x900")
    window.title("Add")
    window.iconbitmap("logo.ico")
    bg10=ImageTk.PhotoImage(file="menu.png")
    bglb10=tk. Label(window,image=bg10)
    bglb10.place(x=-25,y=-50,width=1600,height=900)
    menu(window)
    frm_form9 = tk.Frame(bg="White",relief=tk.FLAT, borderwidth=0)
    frm_form9.pack()
    frm_form9.place(x=500,y=232)
    l1=tk.Label(frm_form9,text='Product ID.',bg='white',fg='#081229')
    l1.config(font=("Times New Roman","20","bold"))
    l1.grid(row=0,column=0)
    e1=tk.Entry(frm_form9,width=25,border=1)
    e1.config(font=("Times New Roman","15","bold"),bg='white',fg='#081229')
    e1.grid(row=0,column=1)
    e2=tk.Entry(frm_form9,width=25,border=1)
    e2.config(font=("Times New Roman","15","bold"),bg='white',fg='#081229')
    e2.grid(row=1,column=1)
    l2=tk.Label(frm_form9,text='Product Name',bg='white',fg='#081229',font=("Times New Roman","20","bold"))
    l2.grid(row=1,column=0)
    l3=tk.Label(frm_form9,text='Quantity',bg='white',fg='#081229',font=("Times New Roman","20","bold"))
    l3.grid(row=2,column=0)
    e3=tk.Entry(frm_form9,width=25,border=1)
    e3.config(font=("Times New Roman","15","bold"),bg='white',fg='#081229')
    e3.grid(row=2,column=1)
    button2=tk.Button(window,text="SUBMIT",command=lambda:submit(),font=("Times New Roman","15","bold"),fg="white",bg="#081229")
    button2.place(x=650,y=380)
    window.mainloop()
def menu(window):
    def logout(window):
        try:
            myc.execute("truncate table login")
            mydb.commit()
            login(window)
        except:
            mydb.rollback()
    reg=tk.Label(text="AVANT INVENTORY",font=("GEORGIA",35,"bold"),fg="#081229",bg="white")
    reg.pack()
    reg.place(x=450,y=70)
    button6=tk.Button(window,text="Add Item",command=lambda:add(window),relief=tk.FLAT,font=("Times New Roman","20","bold"),fg="white",bg="#081229")
    button6.place(x=85,y=200)
    button6=tk.Button(window,text=" Update Item",command=lambda:update(window),relief=tk.FLAT,font=("Times New Roman","20","bold"),fg="white",bg="#081229")
    button6.place(x=75,y=270)
    button6=tk.Button(window,text=" Remove Item",command=lambda:remove(window),relief=tk.FLAT,font=("Times New Roman","20","bold"),fg="white",bg="#081229")
    button6.place(x=75,y=340)
    button6=tk.Button(window,text="Storage",command=lambda:storage(window),relief=tk.FLAT,font=("Times New Roman","20","bold"),fg="white",bg="#081229")
    button6.place(x=90,y=410)
    button6=tk.Button(window,text="Browse",command=lambda:browse(window),relief=tk.FLAT,font=("Times New Roman","20","bold"),fg="white",bg="#081229")
    button6.place(x=90,y=480)
    button6=tk.Button(window,text="Logout",command=lambda:logout(window),font=("Times New Roman","15","bold"),fg="#081229",bg="white")
    button6.place(x=1100,y=2,width=70,height=30)
def Home(window):
    window=tk.Tk()
    window.geometry("1600x900")
    window.title("Page")
    window.iconbitmap("logo.ico")
    bg10=ImageTk.PhotoImage(file="menu.png")
    bglb10=tk. Label(window,image=bg10)
    bglb10.place(x=-25,y=-50,width=1600,height=900)
    menu(window)
    window.mainloop()
def login(window):
    window.destroy()
    def submit(window):
        g67=e1.get()
        f67=e2.get()
        myc.execute("Select empno from employee")
        k67=myc.fetchall()
        r67=[]
        for i67 in k67:
            for j67 in i67:
                r67.append(j67)
        if g67=='' or f67=='':
            messagebox.showerror("Error","All Fields Are Required")
        else:
            try:
                g68=int(g67)
                if (g68 not in r67):
                    messagebox.showerror("Error","Empno doesn't Exist")
                elif (g68 in r67):
                        myc.execute("Select password from employee where empno={}".format(g68))
                        k68=myc.fetchone()
                        va68=''
                        for i68 in k68:
                            va68=va68+i68
                        if f67!=va68:
                            messagebox.showerror("Error","Incorrect Password")
                        else:
                           myc.execute("Select name from employee where empno={}".format(g68))
                           k69=myc.fetchone()
                           va69=''
                           for i69 in k69:
                               va69=va69+i69
                           try:
                               myc.execute("INSERT INTO login values({},'{}','{}')".format(g68,f67,va69))
                               messagebox.showinfo("Login","Login Succesful")
                               mydb.commit()
                               window.destroy()
                               Home(window)
                           except:
                               mydb.rollback()
                               messagebox.showerror("Error","Login Unsuccessful")
            except:
                messagebox.showerror("Error","Empno should be an integer")
    def show():
        if(c_v1.get()==1):
            e2.config(show='')
        else:
            e2.config(show='*') 

    def chome4():
        window.destroy()
        main()      
    window=tk.Tk()
    window.geometry('1600x900')
    window.title('LOGIN')
    window.iconbitmap("logo.ico")
    bg=ImageTk.PhotoImage(file="login.png")
    bglb=tk.Label(window,image=bg)
    bglb.place(x=-50,y=-50,width=1600,height=900)
    l3=tk.Label(window,text='Staff',bg='white',fg='#081229',width=10)
    l3.config(font=("Times New Roman","60","bold"))
    l3.place(x=390,y=150)
    l1=tk.Label(window,text='Emp No.',bg='white',fg='#081229')
    l1.config(font=("Times New Roman","20","bold"))
    l1.place(x=400,y=300)
    e1=tk.Entry(window,width=25,border=1)
    e1.config(font=("Times New Roman","15","bold"),bg='white',fg='#081229')
    e1.place(x=525,y=305)
    e2=tk.Entry(window,width=25,border=1,show='*')
    e2.config(font=("Times New Roman","15","bold"),bg='white',fg='#081229')
    e2.place(x=525,y=350)
    l2=tk.Label(window,text='Password',bg='white',fg='#081229',font=("Times New Roman","20","bold"))
    l2.place(x=400,y=350)
    c_v1=tk.IntVar(value=0)
    c1 = tk.Checkbutton(window,text='Show Password',variable=c_v1,onvalue=1,offvalue=0,command=show,bg='white')
    c1.place(x=450,y=400)
    button3=tk.Button(window,text="Back To Home",relief=tk.FLAT,command=lambda:chome4(),font=("Times New Roman","20","bold"),fg="#081229",bg="white")
    button3.place(x=430,y=430)
    button46=tk.Button(window,text="Login",relief=tk.FLAT,command=lambda:submit(window),font=("Times New Roman","20","bold"),fg="#081229",bg="white")
    button46.place(x=700,y=430)
    window.mainloop()
def main():
    window=tk.Tk()
    window.title("Home")
    window.iconbitmap("logo.ico")
    window.geometry("1600x900")
    home=ImageTk.PhotoImage(file="BHome.png")
    bg=ImageTk.PhotoImage(file="HOME.jpg")
    bglb=tk.Label(window,image=bg)
    bglb.place(x=-50,y=-50,width=1600,height=900)
    button=tk.Button(window,text="LOGIN",command=lambda:login(window),relief=tk.FLAT,font=("Times New Roman","28","bold"),fg="white",bg="#081229")
    button.place(x=220,y=523)
    window.mainloop()
createdatabase()
createtables()
main()
