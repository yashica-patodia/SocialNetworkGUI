from tkinter import filedialog, _setit
from tkinter.scrolledtext import ScrolledText
from .BackendManager import *
from .UserContactListFrame import *
from .GroupMemberFrame import *
from .MessageAllFrame import *
from tkinter import *
import tkinter.simpledialog


class TkinterGUI:
    def __init__(self, social_network_file, message_file):
        self.root = Tk()
        self.root.title("Social Network")
        self.height = int(self.root.winfo_screenheight() / 1.5)
        self.width = int(self.root.winfo_screenwidth() / 1.5)
        self.root.geometry("{}x{}".format(str(self.width), str(self.height)))
        self.backend_manager = DatabaseManager()
        self.backend_manager.create_user_info(social_network_file)
        self.backend_manager.create_message_info(message_file)

        self.top_frame = Frame(self.root, bg='cyan', width=str(self.width), height=str(int(self.height) / 1.2))
        self.bottom_frame = Frame(self.root, bg='gray2', width=str(self.width), height=str(int(self.height / 6)))
        self.top_frame.pack(side=TOP)
        self.bottom_frame.pack(side=BOTTOM)
        self.top_frame.pack_propagate(0)
        self.bottom_frame.pack_propagate(0)

        self.contact_list_frame = Frame(self.top_frame, bg='blue', width=str(int(self.width / 3)),
                                        height=str(int(self.height / 1.2)))
        self.group_list_frame = Frame(self.top_frame, bg='orange', width=str(int(self.width / 3)),
                                      height=str(int(self.height / 1.2)))
        self.message_list_frame = Frame(self.top_frame, bg='green', width=str(int(self.width / 3)),
                                        height=str(int(self.height / 1.2)))
        self.contact_list_frame.pack(side=LEFT)
        self.group_list_frame.pack(side=LEFT)
        self.message_list_frame.pack(side=LEFT)
        self.contact_list_frame.pack_propagate(0)
        self.group_list_frame.pack_propagate(0)
        self.message_list_frame.pack_propagate(0)

        self.heading_1 = Label(self.contact_list_frame, text="Contact List")
        self.heading_1.pack(padx=5)
        self.heading_2 = Label(self.group_list_frame, text="Group List")
        self.heading_2.pack(padx=5)
        self.heading_3 = Label(self.message_list_frame, text="Messages Received")
        self.heading_3.pack(padx=5)

        self.bottom_frame1 = Frame(self.bottom_frame, bg='purple', width=str(self.width),
                                   height=str(int(self.height / 12)))
        self.bottom_frame2 = Frame(self.bottom_frame, bg='cyan', width=str(self.width),
                                   height=str(int(self.height / 12)))
        self.bottom_frame1.pack(side=TOP)
        self.bottom_frame2.pack(side=TOP)
        self.bottom_frame1.pack_propagate(0)
        self.bottom_frame2.pack_propagate(0)

        self.choose_user_frame = LabelFrame(self.bottom_frame2, text="Choose User", bg='black', fg='white')
        self.choose_user_frame.pack(side=LEFT, padx=15, pady=1)
        self.tkinter_variable = StringVar(self.choose_user_frame)
        self.tkinter_variable.set("User List")
        self.tkinter_variable.trace("w", self.find_user_info)
        # user_list = []
        # for i in self.backend_manager.all_users:
        #     user_list.append(i)
        self.option_menu = OptionMenu(self.choose_user_frame, self.tkinter_variable,
                                      *tuple(self.backend_manager.all_users))
        self.option_menu.pack()

        self.message_variable = StringVar()
        self.message_text = Entry(self.bottom_frame1, textvariable=self.message_variable)
        # str2=""
        # self.message_text.insert(str2)
        self.message_text.pack(side=LEFT, padx=5)

        self.message_send_button = Button(self.bottom_frame1, text="SEND", bg='black', fg='white',
                                          command=self.send_msg)
        self.message_send_button.pack(side=LEFT, padx=5)

        self.receiver_variable = StringVar(self.bottom_frame1)
        self.receiver_variable.set("Contact List")
        my_receiver_list = []
        self.receiver_menu = OptionMenu(self.bottom_frame1, self.receiver_variable, ())
        self.receiver_menu.pack(side=LEFT, padx=5)

        self.image_button = Button(self.bottom_frame1, text="Send Img", command=self.load_image)
        self.image_button.pack(side=LEFT, padx=5)
        self.image_message = StringVar()
        self.image_message.set("")
        self.image_label = Label(self.bottom_frame1, textvariable=self.image_message)

        self.image_label.pack(side=LEFT, padx=5)

    def load_image(self):
        image_filename = filedialog.askopenfilename(title='Image')
        self.image_message.set(image_filename)

    def send_msg(self):
        message_tx = self.message_variable.get()
        self.backend_manager.send_message(message_tx, self.image_message.get(), self.receiver_variable.get())
        self.image_message.set("")
        self.message_variable.set("")

    def hide_all_frames(self):
        # for widget in self.contact_list_frame.winfo_children():
        #     widget.destroy()
        # for widget in self.message_list_frame.winfo_children():
        #     widget.destroy()
        # for widget in self.group_list_frame.winfo_children():
        #     widget.destroy()
        pass

    def find_user_info(self, *args):
       # print("enter pls here")
        for widget in self.contact_list_frame.winfo_children():
            widget.destroy()
        for widget in self.message_list_frame.winfo_children():
            widget.destroy()
        for widget in self.group_list_frame.winfo_children():
            widget.destroy()
        self.hide_all_frames()
        #print("enter here 2")
        cur_user = self.tkinter_variable.get()
        if cur_user not in self.backend_manager.all_users:
            print("not here")
            return None
        self.backend_manager.current_user = self.backend_manager.all_users[cur_user]
        #print(cur_user)
        user = self.backend_manager.all_users[cur_user]
        print(user.contact_list)
        print(user.group_list)
        print(user.received_msg)
        contact_list_frame = UserContactListFrame(self.contact_list_frame, user.contact_list, self.height, self.width)
        #print("1")
        group_list_frame = GroupMemberFrame(user.group_list, self.group_list_frame, self.height, self.width)
        #print("2")
        message_list_frame = MesssageAllFrame(user.received_msg, self.message_list_frame, self.height, self.width)
        #print("3")
        contact_list_frame.pack()
        group_list_frame.pack()
        message_list_frame.pack()
        #print("enter here 3")
        self.receiver_variable.set('')
        self.receiver_menu['menu'].delete(0, 'end')
        #print("in gui")
        print(user.contact_list)
        print(user.group_list)
        for contact in user.contact_list:
            self.receiver_menu['menu'].add_command(label=contact, command=_setit(self.receiver_variable, contact))
        for group in user.group_list:
            self.receiver_menu['menu'].add_command(label=group, command=_setit(self.receiver_variable, group))
        self.receiver_variable.set("Send this user")

    def run(self):
        self.root.mainloop()
