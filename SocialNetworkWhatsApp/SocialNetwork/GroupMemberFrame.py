from tkinter.scrolledtext import ScrolledText

from .GroupFrame import *
from tkinter import *


class GroupMemberFrame(Frame):
    def __init__(self, group_member_list, parent, height, width):
        Frame.__init__(self, parent)
        self.group_member_list = group_member_list
        self.height = height
        self.width = width
        list_scroll = ScrolledText(self, bg='orange', fg='white', width=self.width, height=self.height)
        for member_id in self.group_member_list:
            list_scroll.window_create(END, window=GroupFrame(self.group_member_list[member_id], self))
            list_scroll.insert(END, '\n')
        list_scroll.pack()
        # GroupFrame(self.group_member_list[member_id], self).pack()
