from tkinter import *
import gui.theme as theme
from PIL import Image, ImageTk


class Header:
    def __init__(self):
        self.headerframe=None
        self.LogoFrame=None
        self.ProjectTitle=None
        self.SubTitle=None
        self.LogoImage=None

    def Creater_Header(self,window):
        self.Create_headerframe(window)
        self.Create_Picture()
        self.Create_Title()
        self.Create_SubTite()
        self.Pack_Widgets()


    def Create_headerframe(self,window):
        self.headerframe=Frame(window,height=80,bg=theme.HEADER_BACKGROUND)



    def Create_Picture(self):

        image = Image.open("assets/logo/logo.png")
        image = image.resize((70, 70))
        Logo_image = ImageTk.PhotoImage(image)

        self.LogoImage=Logo_image # keep the reference of picture
        self.LogoPicture=Label(self.headerframe,image=Logo_image,relief="flat",bd=0)



    def Create_Title(self):

       self.ProjectTitle=Label(self.headerframe,bg=theme.HEADER_BACKGROUND,text="AI FAQ Assistant")
       self.ProjectTitle.config(font=theme.HEADER_TITLE_FONT,fg="White")



    def Create_SubTite(self):
       self.SubTitle=Label(self.headerframe,bg=theme.HEADER_BACKGROUND,fg="Gray",font=theme.HEADER_SUBTITLE_FONT)
       self.SubTitle.config(text="Smart answers from your personalized knowledge base.")




    def Pack_Widgets(self):
       
       self.headerframe.pack(fill="x")
       self.headerframe.pack_propagate(False)

       self.LogoPicture.pack(side="left",padx=20,anchor="w")
       self.LogoPicture.pack_propagate(False)

       self.ProjectTitle.pack(side="top",anchor="w",padx=10,pady=3)
       self.SubTitle.pack(side="bottom",anchor="w",padx=10,pady=8)


