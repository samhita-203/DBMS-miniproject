# import modules
from tkinter import *
import sqlite3
import tkinter.messagebox
# connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move around the databse
c = conn.cursor()

# empty list to later append the ids from the database
ids = []

# tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        # labels for the window
        self.heading = Label(self.left, text="Hospital Appointments", font=('arial 40 bold'), fg='black', bg='lightgreen')
        self.heading.place(x=0, y=0)
        # patients name
        self.Name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.Name.place(x=0, y=100)

        # age
        self.Age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.Age.place(x=0, y=140)

        # gender
        self.Gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.Gender.place(x=0, y=180)

        # location
        self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.location.place(x=0, y=220)

        # phone
        self.Phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.Phone.place(x=0, y=260)

        self.scheduled_time = Label(self.left, text="Scheduled Time", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.scheduled_time.place(x=0, y=300)

        # Entries for all labels============================================================
        self.Name_ent = Entry(self.left, width=30)
        self.Name_ent.place(x=250, y=100)

        self.Age_ent = Entry(self.left, width=30)
        self.Age_ent.place(x=250, y=140)
    
        self.Gender_ent = Entry(self.left, width=30)
        self.Gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.Phone_ent = Entry(self.left, width=30)
        self.Phone_ent.place(x=250, y=260)

        self.scheduled_time_ent = Entry(self.left, width=30)
        self.scheduled_time_ent.place(x=250, y=300)

        # button to perform a command
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=340)
    
        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)
        
        # ordering the ids
        self.new = sorted(ids)
        self.final_id = range(0,6)
        # displaying the logs in our right frame
        self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total Appointments till now :  " + str(self.final_id))
    # funtion to call when the submit button is clicked
    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.Name_ent.get()
        self.val2 = self.Age_ent.get()
        self.val3 = self.Gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.Phone_ent.get()
        self.val6 = self.scheduled_time_ent.get()

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '' or self.val6 == '' :
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            sql = "INSERT INTO 'appointments' (Name, Age, Gender, location, Phone, scheduled_time) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for " +str(self.val1) + " has been created" )
            

            self.box.insert(END, 'Appointment fixed for ' + str(self.val1) + ' at ' + str(self.val6))

# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()