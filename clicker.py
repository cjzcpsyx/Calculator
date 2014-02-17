from Tkinter import *
clicks = 1
def click():
	global clicks
	global window
	global label
	clicks = clicks * 10 + 5
	label.config(text = str(clicks))
window = Tk()
label = Label(window, text = str(clicks))
label.pack()
button = Button(window, text='click me!', command= click).pack()
window.mainloop()
