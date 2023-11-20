from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3

database_password = 'university of misurata database'
admin_name= 'admin'
admin_password= 'admin'

def forgot_password():
    global admin_name
    global admin_password
    window = Tk()
    window.title('Login Window!')
    window.geometry('550x300')
    window.resizable(0,0)

    TopViewForm = Frame(window, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    
    lbl_text = Label(TopViewForm, text="New Name & Password", font=('arial', 20), bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)

    Label(window, text= 'Database Password', font=("Arial Bold", 18)).place(x=40, y=80)
    txt_db = Entry(window, width= 40)
    txt_db.place(x= 280, y= 90)
    txt_db.focus_set()

    Label(window, text= 'New Name', font=("Arial Bold", 18)).place(x=40, y=120)
    txt_name = Entry(window, width= 40)
    txt_name.place(x= 280, y= 130)

    Label(window, text= 'New Password', font=("Arial Bold", 18)).place(x=40, y=160)
    txt_password = Entry(window, show='*', width=40)
    txt_password.place(x= 280, y=170)

    def commiting():
        global admin_password
        global admin_name
        if(txt_db.get() == database_password):
            
            admin_name = txt_name.get()
            admin_password = txt_password.get()
            window.destroy()
            login_window()
        else:
            Label(window, text="Invalid Database password!\nPlease try again", fg="red").place(x=210, y=255)

    Button(window, text='Commit Cahnges', font=14, bg="#1C2833",fg="white", command=commiting).place(x=220, y=220)
    window.mainloop()

def search_for(id):
    window = Tk()
    window.title("Search For!")
    window.geometry('800x400')
    window.resizable(0,0)

    connection = sqlite3.connect('university_database.db')
    cursor = connection.execute(f"select * from students where name = '{id}' or id = '{id}'")
    cursor1 = connection.execute(f"select * from instructors where name = '{id}' or id = '{id}'")
    cursor2 = connection.execute(f"select * from employees where name = '{id}' or id = '{id}'")
    def DisplayData():
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        fetch = cursor1.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        fetch = cursor2.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        cursor1.close()
        cursor2.close()
        connection.commit()
    global tree

    TopViewForm = Frame(window, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    
    MidViewForm = Frame(window, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text=f"Search Results For {id}", font=('arial', 20), width=600,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)
    tree = ttk.Treeview(MidViewForm,columns=("id", "name", "college_name", "department","join_date"),selectmode="extended", height=120)

    tree.heading('id', text="ID Number", anchor=W)
    tree.heading('name', text="Name", anchor=W)
    tree.heading('college_name', text="College Name", anchor=W)
    tree.heading('department', text="Department", anchor=W)
    tree.heading('join_date', text="Join Date", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=2)
    tree.column('#1', stretch=NO, minwidth=0, width=85)
    tree.column('#2', stretch=NO, minwidth=0, width=190)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=210)
    tree.pack()
    DisplayData()

    window.mainloop()

def del_person(id):
    connection = sqlite3.connect('university_database.db')
    cursor = connection.execute(f"delete from students where name = '{id}' or id = '{id}'")
    cursor1 = connection.execute(f"delete from instructors where name = '{id}' or id = '{id}'")
    cursor2 = connection.execute(f"delete from employees where name = '{id}' or id = '{id}'")
    cursor.close()
    cursor1.close()
    cursor2.close()
    connection.commit()
    messagebox.showinfo('Alert!', 'Deleted Successfully')

def adding_data():
    window = Tk()
    window.title("Database")
    window.geometry('650x440')
    window.resizable(0,0)

    TopViewForm = Frame(window, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)

    lbl_text = Label(TopViewForm, text="Fill the follwoing fields", font=('arial', 20), width=600, height=4,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)

    Label(window, text="Person", font=("Arial Bold", 16)).place(x=30, y=140)
    combo = ttk.Combobox(window, state='readonly', width=17)
    combo.place(x=200, y= 145)
    combo['values'] = ("student","instructor","employee")
    combo.current(0)

    Label(window, text="ID Number", font=("Arial Bold", 16)).place(x=30, y=180)
    txt_id = Entry(window, width=20)
    txt_id.place(x=200, y=185)

    Label(window, text="Name", font=("Arial Bold", 16)).place(x=30, y=220)
    txt_name = Entry(window, width=40)
    txt_name.place(x=200, y=225)

    Label(window, text="College Name", font=("Arial Bold", 16)).place(x=30, y=260)
    txt_college = Entry(window, width=40)
    txt_college.place(x=200, y=265)

    Label(window, text="Department", font=("Arial Bold", 16)).place(x=30, y=300)
    txt_dept = Entry(window, width=40)
    txt_dept.place(x=200, y=305)

    Label(window, text="Join Date", font=("Arial Bold", 16)).place(x=30, y=340)
    txt_date = Entry(window, width=20)
    txt_date.place(x=200, y=345)

    def save_value():
        id = txt_id.get()
        name = txt_name.get()
        college = txt_college.get()
        department = txt_dept.get()
        join_date = txt_date.get()
        prv_win = combo.get()
        
        if(prv_win == 'student'):
            try:
                connection = sqlite3.connect('university_database.db')
                cursor = connection.cursor()
                sql = "INSERT INTO students (id, name, college_name, department, join_date) VALUES (?,?,?,?,?);"
                my_data = (id, name, college, department, join_date)
                cursor.execute(sql, my_data)
                connection.commit()
                connection.close()
            except:
                messagebox.showinfo('Alert!','Something went wrong\nUNIQUE constrain faild')
        elif(prv_win == 'instructor'):
            try:
                connection = sqlite3.connect('university_database.db')
                cursor = connection.cursor()
                sql = "INSERT INTO instructors (id, name, college_name, department, join_date) VALUES (?,?,?,?,?);"
                my_data = (id, name, college, department, join_date)
                cursor.execute(sql, my_data)
                connection.commit()
                connection.close()
            except:
                messagebox.showinfo('Alert!','Something went wrong\nUNIQUE constrain faild')
        elif(prv_win == 'employee'):
            try:
                connection = sqlite3.connect('university_database.db')
                cursor = connection.cursor()
                sql = "INSERT INTO employees (id, name, college_name, department, join_date) VALUES (?,?,?,?,?);"
                my_data = (id, name, college, department, join_date)
                cursor.execute(sql, my_data)
                connection.commit()
                connection.close()
            except:
                messagebox.showinfo('Alert!','Something went wrong\nUNIQUE constrain faild')
        
        txt_id.delete(0, END)
        txt_name.delete(0, END)
        txt_college.delete(0,END)
        txt_dept.delete(0,END)
        txt_date.delete(0,END)

    
    btn_add = Button(window, text = "Add", width=10, bg="#1C2833",fg="white", command= save_value)
    btn_add.place(x= 50, y= 390)
    btn_back = Button(window, text="Back", width=10, bg="#1C2833",fg="white", command=lambda:[window.destroy(), home_window()])
    btn_back.place(x=500, y=390)

    window.mainloop()

def login_window():
    window = Tk()
    window.title('Login Window!')
    window.geometry('550x500')
    window.resizable(0,0)

    TopViewForm = Frame(window, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    
    lbl_text = Label(TopViewForm, text="Univerity of Misurata\nPlease enter details below", font=('arial', 20), bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)

    img = PhotoImage(file='user.png')
    img_lbl = ttk.Label(window, image=img)
    img_lbl.place(x=200, y=95)

    Label(window, text= 'Name', font=("Arial Bold", 18)).place(x=80, y=240)
    txt_name = Entry(window, width= 30)
    txt_name.place(x= 280, y= 250)
    txt_name.focus_set()

    Label(window, text= 'Password', font=("Arial Bold", 18)).place(x=80, y=300)
    txt_password = Entry(window, show='*', width=30)
    txt_password.place(x= 280, y=310)

    def log_in():
        if(txt_name.get() == admin_name and txt_password.get() == admin_password):
            window.destroy()
            home_window()
        else:
            Label(window, text="Invalid name or password!\nPlease try again", fg="red").place(x=205, y=410)

    Label(window, text='Fill the empty fields!!!', font=14).place(x=200, y=340)
    Button(window, text='Log-in', width=15, bg="#1C2833",fg="white", command= log_in).place(x=220, y=375)
    Button(window, text='Cancle', width=10, command=window.destroy).place(x=40, y=450)
    Button(window, text = 'Forogt Password?', borderwidth=0, command= lambda:[window.destroy(), forgot_password()]).place(x=230, y=450)
    window.mainloop()
      
def home_window():
    window = Tk()
    window.title("Home Window!")
    window.geometry('650x350')
    window.resizable(0,0)

    TopViewForm = Frame(window, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    
    lbl_text = Label(TopViewForm, text="Univerity of Misurata\nData Base", font=('arial', 20), height=5, bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)

    img = PhotoImage(file='search.png')
    img_lbl = ttk.Label(window, image=img)
    img_lbl.place(x=20, y=135)
    txt_search = Entry(window, width=45)
    txt_search.place(x=60, y=138)
    btn_search = Button(window, text="Search", width=10, command=lambda:[search_for(txt_search.get())])
    btn_search.place(x=390, y=135)
    btn_delete = Button(window, text='Delete', width=10, command= lambda:[del_person(txt_search.get())])
    btn_delete.place(x=490, y=135)
    
    btn_students = Button(window, width=30, text = "Display Students", font=('bold',16), command= lambda:[window.destroy(), students_window()])
    btn_students.place(x= 150, y= 180)

    btn_instructors = Button(window, width=30, text = "Display Instructors", font=('bold',16), command= lambda:[window.destroy(), instructors_window()])
    btn_instructors.place(x= 150, y= 220)

    btn_employees = Button(window, width=30, text = "Display Employees", font=('bold',16), command= lambda:[window.destroy(), employees_window()])
    btn_employees.place(x= 150, y= 260)

    btn_add = Button(window, width=30, text='New Person', font=('bold',16), command=lambda: [window.destroy(), adding_data()])
    btn_add.place(x= 150, y= 300) 
    window.mainloop()

def students_window():
    window = Tk()
    window.title("Students Window!")
    window.geometry('800x400')
    window.resizable(0,0)
    
    def DisplayData():
        connection = sqlite3.connect('university_database.db')
        cursor = connection.execute("SELECT * FROM students")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        connection.close()
    global tree

    TopViewForm = Frame(window, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    
    MidViewForm = Frame(window, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Records Of Students", font=('arial', 20), width=600,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)
    tree = ttk.Treeview(MidViewForm,columns=("id", "name", "college_name", "department","join_date"),selectmode="extended", height=120)

    tree.heading('id', text="ID Number", anchor=W)
    tree.heading('name', text="Name", anchor=W)
    tree.heading('college_name', text="College Name", anchor=W)
    tree.heading('department', text="Department", anchor=W)
    tree.heading('join_date', text="Join Date", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=2)
    tree.column('#1', stretch=NO, minwidth=0, width=85)
    tree.column('#2', stretch=NO, minwidth=0, width=190)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=210)
    tree.pack()
    DisplayData()

    btn_home = Button(window, text="Home", width=10, bg="#1C2833",fg="white", command= lambda:[window.destroy(), home_window()])
    btn_home.place(x=650, y=350)

    window.mainloop()

def instructors_window():
    window = Tk()
    window.title("Instructors Window!")
    window.geometry('800x400')
    window.resizable(0,0)
    
    def DisplayData():
        connection = sqlite3.connect('university_database.db')
        cursor = connection.execute("SELECT * FROM instructors")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        connection.close()
    global tree

    TopViewForm = Frame(window, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    
    MidViewForm = Frame(window, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Records Of Instructors", font=('arial', 20), width=600,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)
    tree = ttk.Treeview(MidViewForm,columns=("id", "name", "college_name", "department","join_date"),selectmode="extended", height=120)

    tree.heading('id', text="ID Number", anchor=W)
    tree.heading('name', text="Name", anchor=W)
    tree.heading('college_name', text="College Name", anchor=W)
    tree.heading('department', text="Department", anchor=W)
    tree.heading('join_date', text="Join Date", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=2)
    tree.column('#1', stretch=NO, minwidth=0, width=85)
    tree.column('#2', stretch=NO, minwidth=0, width=190)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=210)
    tree.pack()
    DisplayData()
    
    btn_home = Button(window, text="Home", width=10, bg="#1C2833",fg="white", command= lambda:[window.destroy(), home_window()])
    btn_home.place(x=650, y=350)

    window.mainloop()

def employees_window():
    window = Tk()
    window.title("Employees Window!")
    window.geometry('800x400')
    window.resizable(0,0)
    
    def DisplayData():
        connection = sqlite3.connect('university_database.db')
        cursor = connection.execute("SELECT * FROM employees")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        connection.close()
    global tree

    TopViewForm = Frame(window, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    
    MidViewForm = Frame(window, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Records Of Employees", font=('arial', 18), width=600,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)
    tree = ttk.Treeview(MidViewForm,columns=("id", "name", "college_name", "department","join_date"),selectmode="extended", height=120)

    tree.heading('id', text="ID Number", anchor=W)
    tree.heading('name', text="Name", anchor=W)
    tree.heading('college_name', text="College Name", anchor=W)
    tree.heading('department', text="Department", anchor=W)
    tree.heading('join_date', text="Join Date", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=2)
    tree.column('#1', stretch=NO, minwidth=0, width=85)
    tree.column('#2', stretch=NO, minwidth=0, width=190)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=210)
    tree.pack()
    DisplayData()
    
    btn_home = Button(window, text="Home", width=10, bg="#1C2833",fg="white", command= lambda:[window.destroy(), home_window()])
    btn_home.place(x=650, y=350)

    window.mainloop()

login_window()