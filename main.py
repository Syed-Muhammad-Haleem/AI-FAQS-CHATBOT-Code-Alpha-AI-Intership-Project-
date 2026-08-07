from tkinter import *
from gui.header import Header
from gui.chat_area import ChatArea
from gui.footer import Footer
from core.dataSet_Loader import DataSetLoader

window=Tk()

window.state("zoomed")


header_Object=Header()
header_Object.Creater_Header(window)


ChatArea_Object=ChatArea()
ChatArea_Object.Create_chatArea(window)


footer_Object=Footer(ChatArea_Object)
footer_Object.Create_Footer(window)

loader = DataSetLoader()
data = loader.load_dataset()

print(data)

window.mainloop()