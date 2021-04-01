from tkinter.scrolledtext import ScrolledText

from .UserFrame import *
from tkinter import *


class UserContactListFrame(Frame):
    def __init__(self, parent, user_contact_list, height, width):
        Frame.__init__(self, parent)
        self.user_contact_list = user_contact_list
        self.height = height
        self.width = width
        list_scroll = ScrolledText(self, bg='blue', fg='white', width=self.width, height=self.height)
        for user_id in self.user_contact_list:
            list_scroll.window_create(END, window=UserFrame(self.user_contact_list[user_id], self))
            list_scroll.insert(END, '\n')
            # UserFrame(self.user_contact_list[user_id],self).pack()
        list_scroll.pack()
