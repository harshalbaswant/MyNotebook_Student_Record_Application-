from tkinter import *
# from reg_form import *
from tkinter import messagebox
from tkinter.messagebox import askyesno


def exit1():
    exit()


def exit2():
    answer = askyesno(title='confirmation',
                      message='Are you sure that you want to quit?')
    if answer:
        exit()


# ******************* register database window ******************************


def reg_form():
    import tkinter as ttk
    from tkinter import messagebox
    from tkinter.messagebox import askyesno
    base = ttk.Tk()

    def fetch():
        name = name_entry.get()
        email = email_entry.get()
        contact = contact_entry.get()
        city = city_entry.get()
        blood = bloodgrp_entry.get()
        password = password_entry.get()

        import pymysql
        myconnect1 = pymysql.connect(host="localhost", user="root", password="Admin123", database="mynotebook")
        value = (name, email, contact, city, blood, password)
        query = "insert into regform(name, email, contact, city, blood_grp, password) value(%s,%s,%s,%s,%s,%s)"
        cursor = myconnect1.cursor()
        cursor.execute(query, value)
        myconnect1.commit()
        print(name, email, contact, city, blood, password)
        messagebox.showinfo("showinfo", "Record saved Successfully!")

        # clear form values

        name_entry.delete(0, END)
        email_entry.delete(0, END)
        contact_entry.delete(0, END)
        city_entry.delete(0, END)
        bloodgrp_entry.delete(0, END)
        password_entry.delete(0, END)

    base.geometry('600x600')
    base.title("MyNotebook Registration Form")
    base.configure(bg='red')
    canvas2 = Canvas(base, width=800, height=700)

    canvas2.pack(fill="both", expand=True)
    bg = PhotoImage(file="RGB1.png")
    canvas2.configure(bg="dodgerblue")
    # canvas2.create_image(0, 0, image=bg, anchor="nw")

    canvas2.create_text(250, 70,  text="Registration form", fill="yellow", font=('roboto black', 30, 'bold'))

    canvas2.create_text(98, 150, text="Name:", fill="yellow", font=('roboto black', 17, 'bold'))

    name_entry = Entry(base, bg="yellow", width=45, highlightthickness=1)
    name_entry.place(x=230, y=142)

    canvas2.create_text(105, 200, text="Email ID:", fill="yellow", font=('roboto black', 16, 'bold'))
    email_entry = Entry(base, bg="yellow", width=45, highlightthickness=1)
    email_entry.place(x=230, y=190)

    canvas2.create_text(119, 250, text="Contact No:", fill="yellow", font=('roboto black', 16, 'bold'))
    contact_entry = Entry(base, bg="yellow", width=45, highlightthickness=1)
    contact_entry.place(x=230, y=240)

    canvas2.create_text(84, 300, text="City:", fill="yellow", font=('roboto black', 16, 'bold'))
    city_entry = Entry(base, bg="yellow", width=45, highlightthickness=1)
    city_entry.place(x=230, y=290)

    canvas2.create_text(123, 350, text="Blood group:", fill="yellow", font=('roboto black', 16, 'bold'))
    bloodgrp_entry = Entry(base, bg="yellow", width=45, highlightthickness=1)
    bloodgrp_entry.place(x=230, y=340)

    canvas2.create_text(112, 400, text="Password:", fill="yellow", font=('roboto black', 16, 'bold'))
    password_entry = Entry(base, bg="yellow", width=45, highlightthickness=1, show='*')
    password_entry.place(x=230, y=390)

    reg = Button(base, text='Cancel', width=15, bg='red', font=("calibri", 13, 'bold'), fg='yellow', command=exit2)
    reg.place(x=50, y=500)

    reg = Button(base, text='Submit', width=15, bg='green', font=("calibri", 13, 'bold'), fg='yellow', command=fetch)
    reg.place(x=400, y=500)

    # it will be used for displaying the registration form onto the window
    base.mainloop()


# reg_form()


# *******************   show database window   ******************************
def show():
    # from tkinter import *
    nn = Tk()
    import pymysql
    from sympy.printing.llvmjitcode import ll

    connect = pymysql.connect(host="localhost", user="root", password="Admin123", database="mynotebook")
    nn.geometry("1400x1000")
    nn.configure(bg='yellow')
    l1 = Label(nn, text="Here Are the List of Records", font=("times new roman bold", 20, "bold"), fg="black",
               bg='yellow')
    l1.place(x=10, y=20)
    query = "select * from regform"
    cur = connect.cursor()
    cur.execute(query)
    connect.commit()
    show1 = cur.fetchall()

    a = 200
    for i in show1:
        b = 10
        for j in i:
            h1 = Label(nn, text=j, font=("times new roman bold", 15, "bold"), fg="black", bg="yellow")
            h1.place(x=b, y=a)
            b = b + 350
        a = a + 60

    nn.mainloop()


# show()

# *******************delete database window ******************************

def delete():
    from tkinter.messagebox import askyesno

    import pymysql

    delete_root = Tk()

    def delete1():
        answer = askyesno(title='confirmation',
                          message='Are you sure that you want to Delete?')
        if answer:
            s_value = search_entry.get()
            connect = pymysql.connect(host="localhost", user="root", password="Admin123", database="mynotebook")
            query = "DELETE FROM regform WHERE name= %s;"
            cursor = connect.cursor()
            cursor.execute(query, s_value)
            connect.commit()
            search_entry.delete(0, END)

    delete_root.geometry("900x500")
    delete_root.title("Remove record")

    delete_root.configure(bg='yellow')
    search1 = Label(delete_root,text='Enter Full name to Delete Record', bg="yellow", font='Aloevera 25 bold')
    search1.place(x=200, y=70)

    warning=Label(delete_root,text="Warning: Deleted Record can't be restored...", fg='red',bg='cyan',font='calibri 15 bold' )
    warning.place(x=250,y=140)
    search_entry = Entry(delete_root,bg="gold1", font=("arial", 15, "bold"), width=60, highlightthickness=1, highlightcolor="green")
    search_entry.place(x=170, y=190)

    reg = Button(delete_root,text='Delete', width=15, bg='red', font=("calibri", 13, 'bold'), fg='white', command=delete1)
    reg.place(x=400, y=260)

    reg = Button(delete_root,text='Exit', width=15, bg='grey', font=("calibri", 13, 'bold'), command=exit1)
    reg.place(x=400, y=450)
    delete_root.mainloop()

# delete()
# *******************  search database window ******************************


def search():
    import tkinter as xx
    dd = xx.Tk()
    dd.geometry("1350x600")
    dd.title('Search Record')
    dd.configure(bg='yellow')
    search1 = xx.Label(dd, text='Enter Full name to Search Record', bg="yellow", font='Aloevera 25 bold')
    search1.place(x=400, y=170)
    # label1 = xx.Label(dd, text="here you can search the particular record", font=("times new roman", 15, "bold"),
    #                   bg="blue", fg="white")
    # label1.place(x=10, y=20)
    # h2 = xx.Label(dd, text="Enter the name", font=("times new roman", 15, "bold"))
    # h2.place(x=400, y=80)
    texti = xx.Entry(dd, width=50, font=("arial", 15, "bold"), bg="white")
    texti.place(x=400, y=250)

    def done():
        import pymysql
        connect = pymysql.connect(host="localhost", user="root", password="Admin123", database="mynotebook")
        query = "select * from regform where name=%s"
        u = texti.get()
        cur = connect.cursor()
        cur.execute(query, u)
        connect.commit()
        show3 = cur.fetchall()
        # l2 = xx.Label(dd, text="here is the details:", font=("times new roman", 15, "bold"), bg="yellow", fg="black")
        # l2.place(x=300, y=450)

        for i in show3:
            m = 10
            for j in i:
                h2 = xx.Label(dd, text=j, font=("times new roman bold", 18, "bold"), fg="red", bg='yellow')
                h2.place(x=m, y=500)
                m = m + 250

    bot1 = xx.Button(dd, text="search", font=("times new roman bold", 13, "bold"), height=2, width=18, bg="grey",
                     fg="black", command=done)
    bot1.place(x=600, y=300)
    bot2 = xx.Button(dd, text="Exit", font=("times new roman bold", 13, "bold"), height=2, width=18, bg="red",
                     fg="yellow",command=exit2)
    bot2.place(x=600, y=550)

    dd.mainloop()


# search()

# from tkinter import *
# import pymysql
#
#
# search_root = Tk()
#
#
# def search():
#     s_value = search_entry.get()
#
#     connect = pymysql.connect(host="localhost", user="root", password="Admin123", database="mynotebook")
#     query = "select * from regform where name=%s"
#     cursor = connect.cursor()
#     cursor.execute(query, s_value)
#     connect.commit()
#     show = cursor.fetchall()
#
#     for i in show:
#         m = 10
#         for j in i:
#             h2 = Label(search_root, text=j, font=("times new roman bold", 15, "bold"), fg="black")
#             h2.place(x=m, y=300)
#             m = m + 200
#
#
# search_root.geometry("700x500")
# search_root.title("search record")
#
# search_root.configure(bg='yellow')
# search1 = Label(search_root,text='Enter Full name to Search Record', bg="yellow", font='Aloevera 25 bold')
# search1.place(x=70, y=70)
#
# search_entry = Entry(search_root,bg="gold1", width=60, highlightthickness=1, highlightcolor="green")
# search_entry.place(x=180, y=190)
#
# reg = Button(search_root,text='Search', width=15, bg='grey', font=("calibri", 13, 'bold'))
# reg.place(x=270, y=260)
# search_root.mainloop()

