class HandlingFile:
    def __init__(self):
        self.social_network_file = ""
        self.snf_present = False
        self.message_file = ""
        self.msg_present = False

    def set_social_network_file(self, social_network_file):
        self.social_network_file = social_network_file
        self.snf_present = True

    def set_message_file(self, message_file):
        self.message_file = message_file
        self.msg_present = True

    @staticmethod
    def find_user_contact_info(line):
        user_unique_id = ""
        contact_list = []
        user_unique_id_start = line.find("<")
        user_unique_id_end = line.find(":")
        len_user = user_unique_id_end - user_unique_id_start - 1
        if user_unique_id_start != -1 and user_unique_id_end != -1 and len_user > 0:
            user_unique_id = line[user_unique_id_start + 1:user_unique_id_end]
            contact_list_start = user_unique_id_end + 2
            contact_list_end = line.find(">")
            contact_list_str = line[contact_list_start:contact_list_end]
            contact_list = contact_list_str.split(", ")
        print("File handling")
        print(user_unique_id)
        print(contact_list)
        return user_unique_id, contact_list


    def read_social_network_file(self):
        if not self.snf_present:
            print("Social network input file is not present")
            return None
        else:
            flag_users = False
            flag_groups = False
            users_list = {}
            groups_list = {}
            list_of_lines = []
            with open(self.social_network_file, 'r') as rf:
                list_of_lines = rf.readlines()
            # print("Printing list of lines")
            # print(list_of_lines)
            file_open = open(self.social_network_file, 'r')
            for line in file_open.readlines():

                if not flag_users and not flag_groups:
                    # print("1")
                    str2 = line[:6]
                    # print(str2)
                    if str2 == "#users":
                        # print("found user")
                        flag_users = True
                elif flag_users and not flag_groups:
                    # print("2")
                    str2 = line[:7]
                    if str2 == "#groups":
                        # print("found groups")
                        flag_groups = True
                    else:
                        # print(line)
                        uu_id, contact_list = self.find_user_contact_info(line)
                        # print("in if lese 2")
                        # print(uu_id)
                        # print(contact_list)
                        users_list[uu_id] = contact_list

                elif flag_users and flag_groups:
                    # print("3")
                    # print("found both")
                    grp_id, group_list = self.find_user_contact_info(line)
                    groups_list[grp_id] = group_list
            print("Reading social network file")
            print(users_list)
            print(groups_list)
            return users_list, groups_list

    def loading_message_file(self):
        if not self.msg_present:
            print("Message file is not present")
            return None
        else:
            list_of_messages = []
            with open(self.message_file, 'r') as rf:
                list_of_messages = rf.readlines()
            print("printing messages")
            print(list_of_messages)
            all_messages_list = []
            for line in list_of_messages:
                print("printing line by line")
                print(line)
                all_messages_list.append(self.convert_line_to_message(line))
            print("Message list")
            print(all_messages_list)
            return all_messages_list

    @staticmethod
    def convert_line_to_message(line):
        message_start_index = line.find("[")
        message_end_index = line.find("]")
        message_update = line[message_start_index + 1:message_end_index]
        message_list = message_update.split(", ")
        sender_id = message_list[0][8:]
        receiver_id = message_list[1][10:]
        message = message_list[2][9:]
        image = message_list[3][7:]
        user_info_res = (sender_id, receiver_id, message, image)
        print("Printing user info")
        print(user_info_res)
        return user_info_res

    def update_message_file(self, message):
        f = open(self.message_file, "a+")
        f.write(message)
