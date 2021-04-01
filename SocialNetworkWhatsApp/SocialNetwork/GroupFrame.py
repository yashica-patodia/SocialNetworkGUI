from tkinter import *


class GroupFrame(Frame):
    def __init__(self, group, parent):
        self.group = group
        self.group_member_list = []
        Frame.__init__(self, parent)
        group_id_label = Label(self, text=self.group.unique_group_id)
        group_id_label.pack(padx=9, pady=9)
