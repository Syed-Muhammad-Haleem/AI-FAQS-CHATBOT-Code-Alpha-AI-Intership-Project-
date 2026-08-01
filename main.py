from tkinter import *
from gui.header import Header

window=Tk()

window.state("zoomed")


headerObject=Header()
headerObject.Creater_Header(window)


window.mainloop()