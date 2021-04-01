from tkinter import *


class UserFrame(Frame):
    def __init__(self, user, parent):
        self.user = user
        self.user_contact_list = []
        Frame.__init__(self, parent)
        user_id_label = Label(self, text=self.user.unique_user_id)
        user_id_label.pack(padx=9, pady=9)
