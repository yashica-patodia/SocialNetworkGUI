class Group:
    def __init__(self, unique_group_id, group_members=None):
        self.unique_group_id = unique_group_id
        self.group_members = {}

    def print_unique_group_id(self, group):
        str2 = "<ID: {}>"
        return str2.format(group.unique_group_id)

    def print_group_members(self, group):
        print("The following are the group members")
        for users in self.group_members:
            str2 = "<ID: {}>"
            return str2.format(users.unique_user_id)

    def print_info(self, group):
        print("The group information is as follows")
        self.print_unique_group_id(group)
        self.print_group_members(group)

    def add_member(self, user):
        self.group_members[user.unique_user_id] = user

    def add_all_members(self, group_member_list):
        for users in group_member_list:
            self.add_member(users)

    def received_msg_group(self, message):
        for users in self.group_members:
            self.group_members[users].receive_message_user(message)
        # self.send_message(message)

    def send_message_grp(self,message):
        pass
