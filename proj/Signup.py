import tkinter as tk
from tkinter import messagebox
import sqlite3
import bcrypt
import Login as l

class Signup:

    @staticmethod
    def validateId(id_entry):
        valid = True
        if id_entry == "":
            messagebox.showinfo("Error","The ID number is empty")
            valid = False
        else:
            digits_number = len(id_entry)
            if not(id_entry.isdigit()):
                messagebox.showinfo("Error","The ID should consist of numbers only")
                valid = False
            if  digits_number != 10:
                messagebox.showinfo("Error","The ID should contain 10 numbers")
                valid = False
        return valid

    def validateName(self):
        valid = True
        if self.f_name_entry.get() == "" or self.l_name_entry.get() == "":
            messagebox.showinfo("Error","complete your full name")
            valid = False
        else:
            if not(self.f_name_entry.get().isalpha()) or not(self.l_name_entry.get().isalpha()):
                messagebox.showinfo("Error","name should consist of alphabet only")
                valid = False
        return valid

    @staticmethod
    def validatePassword(password_entry): #password doesnt have - or + /
        valid = True
        if password_entry == "":
            messagebox.showinfo("Error","Password is empty")
            valid = False
        else:
            if len(password_entry) < 6:
                messagebox.showinfo("Error","Password at least 6 digits or letters")
                valid = False
        return valid

    def validateNumber(self):
        valid = True
        if self.num_entry.get() == "":
            messagebox.showinfo("Error","phone number is empty")
            valid = False
        else:
            phone_numbers = len(self.num_entry.get())
            if not(self.num_entry.get().startswith("05")):
                messagebox.showinfo("Error","number should start with 05")
                valid = False
            if phone_numbers != 10:
                messagebox.showinfo("Error","phone number should contain 10 numbers")
                valid = False
            if not(self.num_entry.get().isdigit()):
                messagebox.showinfo("Error","phone number should contain numbers only")
                valid = False
            return valid

    def validateEmail(self):
        valid = True
        if self.email_entry.get() == "":
            messagebox.showinfo("Error","Email is empty")
            valid = False
        else:
            if not(self.email_entry.get().endswith("@ksu.edu.sa")):
                messagebox.showinfo("Error","Email should ends with @ksu.edu.sa")
                valid = False
            if self.email_entry.get().startswith("@"):
                messagebox.showinfo("Error","complete your email")
        return valid

    def insertDb(self):
        self.c.execute("SELECT * FROM students")
        result = self.c.fetchall()
        for row in result:
            if row[2] == self.id_entry.get():
                messagebox.showinfo("Error","student already exists")
                return
        password = str(self.password_entry.get()).encode()
        hashed = bcrypt.hashpw(password,bcrypt.gensalt())
        self.c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)",(str(self.f_name_entry.get()),str(self.l_name_entry.get()),
                       str(self.id_entry.get()),hashed,str(self.num_entry.get()),str(self.email_entry.get())))
        self.con.commit()
        messagebox.showinfo("welcome","successful account creation")
        #clear information
        self.f_name_entry.delete(0,"end")
        self.l_name_entry.delete(0,"end")
        self.id_entry.delete(0,"end")
        self.password_entry.delete(0,"end")
        self.num_entry.delete(0,"end")
        self.email_entry.delete(0,"end")



    def submit(self):
        id_validation = self.validateId(self.id_entry.get())
        name_validation = self.validateName()
        password_validation = self.validatePassword(self.password_entry.get())
        number_validation = self.validateNumber()
        email_validation = self.validateEmail()
        if not(id_validation and name_validation and number_validation and password_validation
        and email_validation):
            return
        else:
            self.insertDb()

    def __init__(self):
        self.window = tk.Tk()
        self.window.configure(bg="light blue")
        self.window.title("Sign up")
        self.window.geometry('800x800')
        self.window.geometry("+600+200") # to position the window in the center

        #data base
        self.con = sqlite3.connect("student.db") #this object represent our database
        self.c = self.con.cursor()
        # self.c.execute("""CREATE TABLE students (
        #                 firstname text,
        #                 lastname text,
        #                 id text,
        #                 password text,
        #                 phonenum text,
        #                 email text
        #                 )""")
        # self.con.commit()

        # con_admin = sqlite3.connect("admin.db")
        # c_admin = con_admin.cursor()
        # c_admin.execute("""CREATE TABLE admin (
        #                        id text,
        #                        password text
        #                        )""")
        # con_admin.commit()
        # admin_password = "123456789".encode()
        # hashed = bcrypt.hashpw(admin_password,bcrypt.gensalt())
        # c_admin.execute("INSERT INTO admin VALUES (?,?)",("1231231234",hashed))
        # con_admin.commit()



        #main frame
        main_frame = tk.Frame(self.window,bg="light blue")
        main_frame.pack()
        #frame
        info_frame = tk.Frame(main_frame,bg="light blue")
        info_frame.pack(side="left",ipadx=40)
        login_frame = tk.Frame(main_frame)
        login_frame.pack(side="bottom",pady=12)


        #label
        f_name_label = tk.Label(info_frame,text="First Name",bg="light blue")
        l_name_label = tk.Label(info_frame,text="Last Name",bg="light blue")
        id_label = tk.Label(info_frame,text="ID (10 numbers)",bg="light blue")
        password_label = tk.Label(info_frame,text="Password (at least 6)",bg="light blue")
        email_label = tk.Label(info_frame,text="Email (ksu email)",bg="light blue")
        num_label = tk.Label(info_frame,text="Phone Number (begin with 05)",bg="light blue")

        #entry
        self.f_name_entry = tk.Entry(info_frame,width=25)
        self.l_name_entry = tk.Entry(info_frame,width=25)
        self.id_entry = tk.Entry(info_frame,width=25)
        self.password_entry = tk.Entry(info_frame,width=25)
        self.email_entry = tk.Entry(info_frame,width=25)
        self.num_entry = tk.Entry(info_frame,width=25)

        #pack label with entry
        f_name_label.pack()
        self.f_name_entry.pack()
        l_name_label.pack()
        self.l_name_entry.pack()
        id_label.pack()
        self.id_entry.pack()
        password_label.pack()
        self.password_entry.pack()
        num_label.pack()
        self.num_entry.pack()
        email_label.pack()
        self.email_entry.pack()

        #button
        submit_btn = tk.Button(info_frame,text="Submit",height=2,width=10,command=self.submit)
        submit_btn.pack(pady=12)

        ##
        self.buttonBack = tk.Button(login_frame, text='Login', command=self.go_Login,height=2,width=10)

        self.buttonBack.pack()

        #run
        self.window.mainloop()

    def go_Login(self):
        try:
            self.window.destroy()
            l.Login()
        except AttributeError:
            print("circular import")
Signup()