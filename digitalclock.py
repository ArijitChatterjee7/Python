from tkinter import *
from tkinter.ttk import *
from time import strftime 

root = Tk() 
root.title('AAPNA TIME AYEGA') 
 
def time(): 
	string = strftime('%H:%M:%S %p') 
	lbl.config(text = string) 
	lbl.after(1000, time) 

lbl = Label(root, font = ('Times', 70, 'bold'), 
			background = 'BLACK', 
			foreground = 'RED') 

lbl.pack(anchor = 'center') 
time() 

mainloop() 
