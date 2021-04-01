import PIL.Image
from PIL import *
from PIL import ImageTk
from tkinter import *


class MessageFrame(Frame):
    def __init__(self, message, parent):
        Frame.__init__(self, parent)
        self.message = message
        message_frame = LabelFrame(self, text=self.message.sender.unique_user_id)
        message_frame.pack(padx=9, pady=9)
        message_text = Label(message_frame, text=self.message.message)
        message_text.pack()
        if self.message.image_present:
            img = PIL.Image.open(self.message.image_file)
            dimensions = (200, 200)
            img_new = img.resize(dimensions, PIL.Image.ANTIALIAS)
            img_new2 = ImageTk.PhotoImage(img_new)
            image_frame = Label(message_frame, image=img_new2)
            image_frame.image = img_new2
            image_frame.pack()
