from tkinter import *
import gui.theme as theme
from gui.chat_area import  ChatArea

class Footer:
    def __init__(self,ChatArea_Object):
        self.ChatArea_Object=ChatArea_Object
        self.FooterFrame=None
        self.Input_Frame=None
        self.EntryBox=None
        self.SendButton=None
        self.placeholder = "Ask me anything..."
        

    def Create_Footer(self,window):
        self.Create_FooterFrame(window)
        self.Create_Input_Frame()
        self.Create_EntryBox()
        self.Create_SendButton()
        self.Bind_Events()
        self.Pack_Widgets()

    def Create_FooterFrame(self,window):
        self.FooterFrame=Frame(window,bg=theme.CHAT_AREA_BACKGROUND,height=70)

        
    def Create_Input_Frame(self):
        self.Input_Frame=Frame(self.FooterFrame,height=60,bg=theme.HEADER_BACKGROUND)


    def Create_EntryBox(self):
        self.EntryBox=Entry(self.Input_Frame,font=theme.ENTRY_BOX_FONT,width=80,bg="#24241F",fg="White")
        self.EntryBox.insert(0, self.placeholder)


    def Create_SendButton(self):
        self.SendButton=Button(self.Input_Frame,text="➤",font=theme.SEND_BUTTON_FONT,bd = 0,relief="flat",cursor="hand2",command=self.Send_Message_To_CharArea)
        self.SendButton.config(fg = "white",bg = "#2563EB",activebackground = "#1D4ED8",activeforeground = "white")

    def Send_Message_To_CharArea(self):
        Message=self.EntryBox.get()
        self.ChatArea_Object.Create_UserMessage(Message)


    def clear_placeholder(self,event):
        if self.EntryBox.get() == self.placeholder:
          self.EntryBox.delete(0, END)
          self.EntryBox.config(fg="white")


    def add_placeholder(self,event):
      if self.EntryBox.get() == "":
        self.EntryBox.insert(0, self.placeholder)
        self.EntryBox.config(fg="gray")


    def Bind_Events(self):
        self.EntryBox.bind("<FocusIn>", self.clear_placeholder)
        self.EntryBox.bind("<FocusOut>", self.add_placeholder)

    def Pack_Widgets(self):
        self.FooterFrame.pack(fill="x",pady=1)
        self.FooterFrame.pack_propagate(False)
        self.Input_Frame.pack(side="left",padx=240,pady=10)
        self.EntryBox.pack(side="left", padx=5, pady=5,ipady=5,anchor="center")
        self.SendButton.pack(side="right", padx=5, pady=5)
