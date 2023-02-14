import tkinter as tk
import random
import sqlite3
from tkinter import messagebox

class Admin:
   def validateName(self):
      valid = True
      if self.name_entry.get() == "":
         messagebox.showinfo("Error","name is empty")
         valid = False
      else:
          if not(self.name_entry.get().isalpha()):
             messagebox.showinfo("Error","event name must be letters only")
             valid = False
          return valid

   def validateLocation(self):
      valid = True
      if self.location_entry.get() == "":
         messagebox.showinfo("Error","location is empty")
         valid = False
      else:
          if not(self.location_entry.get().isalpha()):
             messagebox.showinfo("Error", "location name must be letters only")
             valid = False
          return valid

   def validateCapacity(self):
      valid = True
      if self.capacity_entry.get() == "":
         messagebox.showinfo("Error","capacity is empty")
         valid = False
      else:
          if not(self.capacity_entry.get().isdigit()):
             messagebox.showinfo("Error", "capacity must be numbers only")
             valid = False
          return valid
   def validateDate(self):
      valid = True
      if self.date_entry.get() == "":
         messagebox.showinfo("Error","date is empty")
         valid = False
      return valid
   def create(self):
      name_validation = self.validateName()
      location_validation = self.validateLocation()
      cap_validation = self.validateCapacity()
      date_validation = self.validateDate()
      if name_validation and location_validation and cap_validation and date_validation:
         ran = random.randint(10000,99999)
         self.c.execute("INSERT INTO evnt VALUES (?,?,?,?,?,?,?)",(str(self.name_entry.get()),str(self.location_entry.get()),str(self.capacity_entry.get())
                                                                  ,str(self.date_entry.get()),str(ran),"0",str(self.time_entry.get())))
         self.con.commit()
         messagebox.showinfo("welcome","successful")

   def __init__(self):
      self.window = tk.Tk()
      self.window.title("Admin")
      self.window.geometry('800x800')
      self.window.configure(bg="light blue")
      #data base 6 columns
      self.con = sqlite3.connect("event.db")
      self.c = self.con.cursor()
      # self.c.execute("""CREATE TABLE evnt (
      #                  name text,
      #                  location text,
      #                  capacity integer,
      #                  date text,
      #                  randomnumbers text,
      #                  bookingnumber integer,
      #                  time text
      #                  )""")
      # self.con.commit()
      #main frame
      main_frame = tk.Frame(self.window,bg="light blue")
      main_frame.pack()
      #frame
      event_frame = tk.Frame(main_frame,bg="light blue")
      event_frame.pack(side="left",ipadx=40)
      logout_frame = tk.Frame(main_frame,bg="light blue")
      logout_frame.pack(side="bottom",pady=12)
      #label
      event_name_label = tk.Label(event_frame,bg="light blue",text="Enter event name")
      event_location_label = tk.Label(event_frame,bg="light blue",text="Enter event location")
      event_capacity_label = tk.Label(event_frame,bg="light blue",text="Enter event capacity")#integer
      event_date_label = tk.Label(event_frame,bg="light blue",text="Enter event date")
      event_time_label = tk.Label(event_frame, bg="light blue", text="Enter event time")
      #entry
      self.name_entry = tk.Entry(event_frame,width=25)
      self.location_entry = tk.Entry(event_frame, width=25)
      self.capacity_entry = tk.Entry(event_frame, width=25)
      self.date_entry = tk.Entry(event_frame, width=25)
      self.time_entry = tk.Entry(event_frame,width=25)
      #pack label with entry
      event_name_label.pack()
      self.name_entry.pack()
      event_location_label.pack()
      self.location_entry.pack()
      event_capacity_label.pack()
      self.capacity_entry.pack()
      event_date_label.pack()
      self.date_entry.pack()
      event_time_label.pack()
      self.time_entry.pack()
      #button
      create_btn = tk.Button(event_frame,text="Create",command=self.create,width=10,height=2)
      create_btn.pack(pady=12)
      #
      self.buttonBack = tk.Button(logout_frame, text='Logout', command=self.logout,width=10,height=2)

      self.buttonBack.pack()
      self.window.mainloop()

   def logout(self):
      self.window.destroy()
      import Signup
      Signup.Signup()

