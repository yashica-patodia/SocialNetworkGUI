from .User import *
from .Group import *
from .HandlingFile import *
from .Message import *


class DatabaseManager:
    def __init__(self):
        self.file_reader = HandlingFile()
        self.all_messages = []
        self.all_users = {}
        self.all_groups = {}
        self.type = {}
        self.current_user = None

    def create_user_info(self, social_network_file):
        self.file_reader.set_social_network_file(social_network_file)
        all_users_info_string, all_groups_info_string = self.file_reader.read_social_network_file()
        print("Create user info")
        print(all_users_info_string)
        print(all_groups_info_string)
        for uu_id in all_users_info_string:
            self.type[uu_id] = 1
            self.all_users[uu_id] = User(uu_id)
        for uu_id in all_users_info_string:
            for i in all_users_info_string[uu_id]:
                if i in self.all_users:
                    continue

                else:
                    self.type[i] = 1
                    self.all_users[i] = User(i)

        for uu_id in all_users_info_string:
            if uu_id in self.all_users:
                self.all_users[uu_id].add_all_contact([self.all_users[i] for i in all_users_info_string[uu_id]])

        for grp_id in all_groups_info_string:
            for i in all_groups_info_string[grp_id]:
                if i in self.all_users:
                    continue
                else:
                    self.type[i] = 1
                    self.all_users[i] = User(i)

        for grp_id in all_groups_info_string:
            # print(grp_id)
            self.all_groups[grp_id] = Group(grp_id)
            self.type[grp_id] = 0
            self.all_groups[grp_id].add_all_members([self.all_users[i] for i in all_groups_info_string[grp_id]])

        # for grp_id in all_groups_info_string:
        #     self.all_groups[grp_id].add_all_members([self.all_users[i] for i in all_groups_info_string[grp_id]])

        for grp_id in all_groups_info_string:
            for member_id in all_groups_info_string[grp_id]:
                if member_id in self.all_users and grp_id in self.all_groups:
                    self.all_users[member_id].add_group(self.all_groups[grp_id])

    def create_message_info(self, message_file):
        self.file_reader.set_message_file(message_file)
        all_messages = self.file_reader.loading_message_file()
        for i in all_messages:
            if i[0] in self.all_users:
                self.all_messages.append(Message(self.all_users[i[0]], i[1], i[2], i[3]))
                if i[1] in self.type and self.type[i[1]] == 1:
                    if i[1] in self.all_users:
                        self.all_users[i[1]].receive_message_user(Message(self.all_users[i[0]], i[1], i[2], i[3]))
                    else:
                        continue
                else:
                    if i[1] in self.all_groups:
                        self.all_groups[i[1]].received_msg_group(Message(self.all_users[i[0]], i[1], i[2], i[3]))
                    else:
                        continue

    def update_current_user(self, user):
        if user in self.all_users:
            self.current_user = self.all_users[user]
        else:
            print("The user id does not exist")

    def send_message(self, message_info, image_file_name, receiver):

        if receiver in self.type:
            if self.type[receiver] == 1:
                if self.current_user.unique_user_id is receiver:
                    print("Cant send message to itself")
                else:
                    message = Message(self.current_user, receiver, message_info, image_file_name)
                    self.all_messages.append(message)
                    self.file_reader.update_message_file(str(message))
                    if receiver in self.all_users:
                        self.all_users[receiver].receive_message_user(message)

            else:
                message = Message(self.current_user, receiver, message_info, image_file_name)
                self.all_messages.append(message)
                self.file_reader.update_message_file(message.print_message())
                if receiver in self.all_groups:
                    self.all_groups[receiver].received_msg_group(message)
