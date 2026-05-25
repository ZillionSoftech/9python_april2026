from tkinter import *

def disp():
    print("Working fine")

root=Tk()
label1=Label(root, text="First Number : ")
label1.pack()

label2=Label(root, text="Second Number : ")
label2.pack()

button1=Button(root, text="ADD", command=root.destroy)
button1.pack()


root.mainloop()