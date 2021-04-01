class User:
    def __init__(self, unique_user_id, contact_list=None, group_list=None, received_msg=None, send_msg=None):
        self.unique_user_id = unique_user_id
        self.contact_list = {}  # [unique_user_id:ContactUser]
        self.group_list = {}
        self.received_msg = []
        self.send_msg = []

    def print_unique_id(self, user):
        st = "<ID: {}>"
        return st.format(user.unique_user_id)

    def print_contact_list(self, user):
        print("The following are in the contact list of user:")
        for contact in user.contact_list:
            self.print_unique_id(contact)

    def print_grp_list(self, user):
        print("The following is the group list of user:")
        for grp in user.group_list:
            self.print_unique_id(grp)

    def print_info(self, user):
        print("The user information is as follows")
        self.print_unique_id(user)
        self.print_contact_list(user)
        self.print_grp_list(user)
        print("------------------------------------------------------------------")

    def __str__(self):
        return "<ID: " + self.unique_user_id + ">"

    def add_contact(self, user):
        self.contact_list[user.unique_user_id] = user

    def add_group(self, group):
        self.group_list[group.unique_group_id] = group

    def add_all_contact(self, contact_list):
        for contact in contact_list:
            self.add_contact(contact)

    def add_all_grp(self, group_list):
        for group in group_list:
            self.add_group(group)

    def receive_message_user(self, message):
        self.received_msg.append(message)

    def send_message(self, message):
        pass
