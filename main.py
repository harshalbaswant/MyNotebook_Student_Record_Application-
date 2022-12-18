# Import module
# import tkinter
from tkinter import *
from more_tab import *

# Create object
root = Tk()

# Adjust size
root.geometry("1110x512")
root.title("MyNotebook Student Record app ")

# Add image file
bg = PhotoImage(file="RGB.png")

# Create Canvas
canvas1 = Canvas(root, width=1110, height=512)
canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 1, image=bg, anchor="nw")

# Add Text
canvas1.create_text(300, 30, text="MyNotebook Student Record Application", fill="yellow", font='Aloevera 21 bold')

# Creating a photoimage object to use image
photo = PhotoImage(file="book.png")

# here, image option is used to
# set image on button-----------second image
Button(root, text='Click Me !', image=photo).place(x=600, y=1)

canvas1.create_text(300, 100, text="NOTE: Press below buttons to perform CRUD operation "
                    , fill="yellow", font='Helvetica 13 bold')

create = Button(text='Register New Record', bg="yellow", font=("calibri", 13, 'bold'), height=2, width=18, command= reg_form)
create.place(x=80, y=160)

search = Button(text='Search Record', bg="yellow", font=("calibri", 13, 'bold'), height=2, width=18,command= search)
search.place(x=350, y=160)


show = Button(text='Show Record', bg="yellow", font=("calibri", 13, 'bold'), height=2, width=18, command=show)
show.place(x=80, y=280)

delete = Button(text='Remove Record', bg="yellow", font=("calibri", 13, 'bold'), height=2, width=18, command=delete)
delete.place(x=350, y=280)

exit = Button(text='Exit Application', bg="yellow", font=("calibri", 13, 'bold'), height=2, width=18, command=exit1)
exit.place(x=200, y=380)

canvas1.create_text(300, 480, text="© 2022 Student Record Application made by- Harshal Baswant "
                    , font='Helvetica 9 bold', fill='black')

# canvas1.create_text(300, 498, text="Thank you - Ankit sir, Nakul sir "
#                     , font='Helvetica 9 bold',fill='black')


# Execute tkinter
root.mainloop()
