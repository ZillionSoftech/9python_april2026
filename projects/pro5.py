from tkinter import *

def disp():
    print("Working fine")

def getValue():
    data=input1.get()
    print(data)

root=Tk()
label1=Label(root, text="First Number : ")
label1.pack()

label2=Label(root, text="Second Number : ")
label2.pack()

button1=Button(root, text="ADD", command=getValue)
button1.pack()

input1=Entry(root)
input1.pack()


root.mainloop()