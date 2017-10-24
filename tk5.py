from tkinter import *
from datetime import datetime
class Timekeeper:
	time_start = None
	time_end = None
	def __init__(self,master):
		frame = Frame(master)
		frame.pack()
		self.label = Label(text = "Click on Start to begin code timing")
		self.label.pack()
		self.button = Button(text="Start",bg="red",command = startCoding)
		self.button.pack()
		
	def startCoding(self):
		global time__start
		time__start = datetime.now()
		self.button['text'] = "End"
		self.button['command'] = startCoding
	def endCoding(self):
		global time__end
		time__end = datetime.now()
		self.button['text'] = "Start"
		self.button['command'] = endCoding
		
root = Tk()
master = Timekeeper(root)
root.mainloop()