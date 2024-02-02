from tkinter import *
root= Tk()
#order widthxheigth
root.geometry("733x434")

#order max width
root.maxsize(1200,988)

#order width,heigth
root.minsize(733,434)

#label 
akshay=Label(text="Akshay is a great person this is his GUI")
akshay.pack()

root.mainloop()