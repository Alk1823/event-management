import tkinter as tk
from tkinter import messagebox
import sqlite3
import bcrypt
import Signup as s
import Admin as ad
import Student as stu

class Login:

    def validate(self):
        id_validation = s.Signup.validateId(self.id_entry.get())
        password_validation = s.Signup.validatePassword(self.password_entry.get())
        if id_validation and password_validation:
            con = sqlite3.connect("student.db")
            c = con.execute("SELECT * FROM students")
            result = c.fetchall()
            new_result = ()
            isFound_student = False
            for row in result:
                if row[2] == self.id_entry.get():
                    new_result = row
                    isFound_student = True
            con_admin = sqlite3.connect("admin.db")
            c_admin = con_admin.cursor()
            c_admin.execute("SELECT * FROM admin")
            resultt = c_admin.fetchall()
            new_resultt = ()
            isFound_admin = False
            for roww in resultt:
                if roww[0] == self.id_entry.get():
                    new_resultt = roww
                    isFound_admin = True
            if isFound_admin or isFound_student:
                if isFound_student:
                    hashed = new_result[3]
                    if not(bcrypt.checkpw(self.password_entry.get().encode(),hashed)):
                        messagebox.showinfo("Error","incorrect password")
                    else:
                        messagebox.showinfo("welcome","successful login")
                        stu.student()

                else:
                    hashed = new_resultt[1]
                    if not(bcrypt.checkpw(self.password_entry.get().encode(),hashed)):
                        messagebox.showinfo("Error","incorrect password")
                    else:
                        messagebox.showinfo("welcome","successful login")
                        ad.Admin()
            else:
                messagebox.showinfo("Error", "there is no user with that id")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.configure(bg="light blue")
        self.window.geometry('800x800')

        #main frame
        main_frame = tk.Frame(self.window,bg="light blue")
        main_frame.pack()
        #frame
        login_frame = tk.Frame(main_frame,bg="light blue")
        login_frame.pack(side="left",ipadx=40)
        signup_frame = tk.Frame(main_frame,bg="light blue")
        signup_frame.pack(side="bottom",pady=12)
        #label
        id_label = tk.Label(login_frame,bg="light blue",text="ID (10 numbers)")
        password_label = tk.Label(login_frame,bg="light blue",text="Password (at least 6)")
        #entry
        self.id_entry = tk.Entry(login_frame,width=25)
        self.password_entry = tk.Entry(login_frame,width=25)
        #pack label with entry
        id_label.pack()
        self.id_entry.pack()
        password_label.pack()
        self.password_entry.pack()
        #btn
        login_btn = tk.Button(login_frame,text="login",height=2,width=10,command=self.validate)
        login_btn.pack(pady=12)
        #
        self.buttonBack = tk.Button(signup_frame, text='Sign up', command=self.go_signup,height=2,width=10)
        self.buttonBack.pack()
        #run
        self.window.mainloop()

    def go_signup(self):
        try:
            self.window.destroy()
            s.Signup()
        except AttributeError:
            print("circular import")
