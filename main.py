from tkinter import *
from gui.header import Header
from gui.chat_area import ChatArea
from gui.footer import Footer
from core.chat_bot import Chat_Bot

window=Tk()

window.state("zoomed")
window.title("FAQs ChatBot")



# the fronted and backend connecter function
def send_message(message):
    
    ChatArea_Object.Create_UserMessage(message)
    answer = ChatBot_Object.get_sent_Return_Function(message)
    
    window.after(
        1000,
        lambda: ChatArea_Object.Create_BotMessage(answer)
    )
    


header_Object=Header()
header_Object.Creater_Header(window)


ChatArea_Object=ChatArea()
ChatArea_Object.Create_chatArea(window)


footer_Object=Footer(send_message)
footer_Object.Create_Footer(window)

ChatBot_Object=Chat_Bot()

window.mainloop()