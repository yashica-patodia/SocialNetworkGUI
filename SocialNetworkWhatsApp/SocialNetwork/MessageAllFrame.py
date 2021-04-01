from tkinter.scrolledtext import ScrolledText

from .MessageFrame import *
from tkinter import *
import tkinter


class MesssageAllFrame(Frame):
    def __init__(self, all_message_list, parent, height, width):
        Frame.__init__(self, parent)
        self.all_msg = all_message_list
        self.height = height
        self.width = width
        list_scroll = ScrolledText(self, bg='black', fg='white', width=self.width, height=self.height)
        for message_user in self.all_msg:
            list_scroll.window_create(END, window=MessageFrame(message_user, list_scroll))
            list_scroll.insert(END, '\n')
            # MessageFrame(self, message_user).pack()
        list_scroll.pack()
