from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox


class student:

    def book(self):
        try:
            row = self.listbox.get(self.listbox.curselection())
            if row[2] > row[5]:
                r = row[4]
                query = """UPDATE evnt SET bookingnumber = bookingnumber + 1 WHERE randomnumbers = ?"""
                self.c.execute(query,(r,))
                self.con.commit()
                messagebox.showinfo("successful","successful book")
                my_tree = ttk.Treeview(self.view)
                my_tree.configure(height=5)
                # define column
                my_tree['column'] = ("name", "location", "capacity", "date", "randomnumbers", "bookingnumber", "time")
                # format column
                my_tree.column("#0", width=120, minwidth=25)
                my_tree.column("name", anchor=W, width=120)
                my_tree.column("location", anchor=W, width=80)
                my_tree.column("capacity", anchor=W, width=80)
                my_tree.column("date", anchor=W, width=80)
                my_tree.column("randomnumbers", anchor=W, width=80)
                my_tree.column("bookingnumber", anchor=W, width=80)
                my_tree.column("time", anchor=W, width=80)
                # heading
                my_tree.heading("#0", text="Label", anchor=W)
                my_tree.heading("name", anchor=W, text="Name")
                my_tree.heading("location", anchor=W, text="Location")
                my_tree.heading("capacity", anchor=W, text="Capacity")
                my_tree.heading("date", anchor=W, text="Date")
                my_tree.heading("randomnumbers", anchor=W, text="event ID")
                my_tree.heading("bookingnumber", anchor=W, text="booking number")
                my_tree.heading("time", anchor=W, text="Time")
                # add data
                my_tree.insert(parent='', index="end", iid=0, text='',
                               values=(row[0], row[1], row[2],row[3],row[4],row[5],
                                       row[6]))
                my_tree.pack()
            else:
                messagebox.showinfo("Error","capacity reached the maximum")
        except TclError:
            print("bad index")


    def __init__(self):
        self.window = Tk()
        self.window.title("student")
        self.window.geometry('800x800')
        self.window.configure(bg="light blue")
        #tab
        notebook = ttk.Notebook(self.window)
        book = Frame(notebook,bg="light blue") #new frame for tab 1
        self.view = Frame(notebook,bg="light blue") #frame for tab 2
        notebook.add(book,text="Book a Ticket")
        notebook.add(self.view,text="View my tickets")
        notebook.pack(expand=True,fill="both")
        #book
        self.listbox = Listbox(book,bg="#f7ffde",width=150)
        self.listbox.pack()
        self.con = sqlite3.connect("event.db")
        self.c = self.con.cursor()
        self.con.commit()
        self.c.execute("SELECT * FROM evnt")
        result = self.c.fetchall()
        for row in result:
            self.listbox.insert(1,row)

        # btn
        book_btn = Button(book, text="Book", width=10, height=2, command=self.book)
        book_btn.pack()
        #
        logout_btn = Button(book, text="Logout", width=10, height=2, command=self.logout)
        logout_btn.pack()



    def logout(self):
        self.window.destroy()
        import Signup
        Signup.Signup()
