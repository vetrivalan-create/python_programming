import tkinter
from tkinter import messagebox
root = tkinter.Tk()


def Onclick_Submit():
    name=name_textbook.get()
    messagebox.showinfo("Captured Data",name)


root.geometry("300x400")
root.configure(bg="#ADD8E6")


root.title("Student Registration Form")
name_label = tkinter.Label(root,text="Enter your Name")
name_label.pack(anchor=tkinter.W,padx=10)

name_textbook = tkinter.Entry(root)
name_textbook.pack(anchor=tkinter.W,padx=10)

email_label = tkinter.Label(root,text="Enter your Email")
email_label.pack(anchor=tkinter.W,padx=10)

email_textbook = tkinter.Entry(root)
email_textbook.pack(anchor=tkinter.W,padx=10)

phone_label = tkinter.Label(root,text="Enter your Phone")
phone_label.pack(anchor=tkinter.W,padx=10)

phone_textbook = tkinter.Entry(root)
phone_textbook.pack(anchor=tkinter.W,padx=10)

submit_button = tkinter.Button(root,text = "Submit",command=Onclick_Submit)
submit_button.pack(anchor=tkinter.W,padx=10)

root.mainloop()