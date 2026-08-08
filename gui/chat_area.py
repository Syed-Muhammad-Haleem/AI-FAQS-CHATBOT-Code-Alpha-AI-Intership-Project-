from tkinter import *
import gui.theme as theme


class ChatArea:
    def __init__(self):
       self.chat_area_frame=None
       self.ChatFrame_Canvas_Container=None
       self.chat_Canvas=None
       self.chat_frame=None
       self.scroll_bar=None

    def Create_chatArea(self,window):

        self.Create_chat_area_frame(window)
        self.Create_ChatFrame_Canvas_Container()
        self.Create_chat_Canvas()
        self.Create_chat_frame()
        self.Create_scroll_bar()
        self.Connect_scrollbar_chat_frame()
        self.Create_BotMessage()
        self.pack_Widgets()

    def Create_chat_area_frame(self,window):
        self.chat_area_frame=Frame(window,bg=theme.CHAT_AREA_BACKGROUND,height=550)
        

    def Create_ChatFrame_Canvas_Container(self):
         self.ChatFrame_Canvas_Container=Frame(self.chat_area_frame,bg=theme.HEADER_BACKGROUND,width=900,height=550)


    def Create_chat_Canvas(self):
        self.chat_Canvas=Canvas(self.ChatFrame_Canvas_Container,bg=theme.HEADER_BACKGROUND,bd=0, highlightthickness=0)
        self.chat_Canvas.config(relief="flat")
       
        
    def Create_chat_frame(self):
        self.chat_frame=Frame(self.chat_Canvas,bg=theme.HEADER_BACKGROUND,width=900,height=550)
        self.chat_Canvas.create_window((0, 0), window=self.chat_frame,anchor="nw")


    def Create_scroll_bar(self):
         self.scroll_bar=Scrollbar(self.chat_area_frame,orient="vertical",width=15,cursor="hand2")
       


    def Connect_scrollbar_chat_frame(self):
        self.chat_Canvas.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.chat_Canvas.yview)
        self.chat_frame.bind("<Configure>",self.Update_ScrollRegion)
        
        
    def Update_ScrollRegion(self, event):
       self.chat_Canvas.configure(scrollregion=self.chat_Canvas.bbox("all"))
        
    
        
    def Create_BotMessage(self,answer="I'm here to help! What do you need?"):
        BotMessage=Label(self.chat_frame,text=answer,bg=theme.BOT_MESSAGE_BACKGROUND,fg="white",font=theme.BOT_MESSAGE_FONT,wraplength=500,justify="left",padx=10,pady=5)
        BotMessage.pack(anchor="w",pady=20,padx=15)
        self.chat_Canvas.update_idletasks()
        self.chat_Canvas.yview_moveto(1.0)


    def Create_UserMessage(self,Message):
        UserMessage=Label(self.chat_frame,text=Message,bg=theme.USER_MESSAGE_BACKGROUND,fg="white",font=theme.BOT_MESSAGE_FONT,wraplength=350,justify="left",padx=10,pady=5)
        UserMessage.pack(anchor="w",pady=20,padx=520)
        self.chat_Canvas.update_idletasks()
        self.chat_Canvas.yview_moveto(1.0)
        
       


    def pack_Widgets(self):
        self.chat_area_frame.pack(fill="x",pady=1)
        self.chat_area_frame.pack_propagate(False)


        self.ChatFrame_Canvas_Container.pack(side="left",padx=220)
        self.ChatFrame_Canvas_Container.pack_propagate(False)

        self.chat_Canvas.pack(side="left",fill="both",expand=True)

    
        self.scroll_bar.pack(side="right",fill="y",padx=5,pady=3)

        
     

       
