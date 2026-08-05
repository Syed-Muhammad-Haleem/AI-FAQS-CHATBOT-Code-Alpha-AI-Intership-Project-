from tkinter import *
import gui.theme as theme

class ChatArea:
    def __init__(self):
       self.chat_Canvas=None
       self.chat_frame=None
       self.scroll_bar=None

    def Create_chatArea(self,window):

        self.Create_chat_Canvas(window)
        self.Create_chat_frame()
        self.Create_scroll_bar()
        self.Connect_scrollbar_chat_frame()
        self.Create_BotMessage()
        self.pack_Widgets()

    def Create_chat_Canvas(self,window):
        self.chat_Canvas=Canvas(window,height=550,bg=theme.CHAT_AREA_BACKGROUND,bd=0, highlightthickness=0)
        self.chat_Canvas.config(relief="flat")
       
        
    


    def Create_chat_frame(self):
        self.chat_frame=Frame(self.chat_Canvas,bg=theme.HEADER_BACKGROUND,width=900,height=1100)
        self.chat_Canvas.create_window((200, 0), window=self.chat_frame,anchor="nw")


    def Create_scroll_bar(self):
         self.scroll_bar=Scrollbar(self.chat_Canvas,orient="vertical",width=15,cursor="hand2")
       


    def Connect_scrollbar_chat_frame(self):
        self.chat_Canvas.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.chat_Canvas.yview)
        self.chat_frame.bind("<Configure>",self.Update_ScrollRegion)
        
        
    def Update_ScrollRegion(self, event):
       self.chat_Canvas.configure(scrollregion=self.chat_Canvas.bbox("all"))
        
    
        
    def Create_BotMessage(self):
        BotMessage=Label(self.chat_frame,text="I'm here to help! What do you need?",bg=theme.CHAT_AREA_BACKGROUND,fg="white",font=theme.BOT_MESSAGE_FONT,wraplength=500,justify="left",padx=10,pady=5)
        BotMessage.pack(anchor="w",pady=20,padx=15)


    def Create_UserMessage(self,Message):
        UserMessage=Label(self.chat_frame,text=Message,bg=theme.CHAT_AREA_BACKGROUND,fg="white",font=theme.BOT_MESSAGE_FONT,wraplength=400,justify="left",padx=10,pady=5)
        UserMessage.pack(anchor="e",pady=20,padx=15)


    def pack_Widgets(self):
        self.chat_Canvas.pack(fill="x",pady=1)
        self.chat_Canvas.pack_propagate(False)

        self.chat_frame.pack_propagate(False)
        self.scroll_bar.pack(side="right",fill="y",padx=5,pady=3)

        
     

       
