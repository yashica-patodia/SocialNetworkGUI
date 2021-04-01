class Message:

    def __init__(self, sender, receiver, message, image_file):
        self.message = message
        self.image_file = image_file
        if image_file == "":
            self.image_present = False
        else:
            self.image_present = True

        self.sender = sender
        self.receiver = receiver

    def print_message(self):
        str_p = "[Sender: {}, Receiver: {}, Message:  {}, Image: {}]\n"
        return str_p.format(self.sender.unique_user_id, self.receiver, self.message, self.image_file)

    def __str__(self):
        prnt = "[Sender: " + self.sender.unique_user_id + ", Receiver: " + self.receiver + ", Message: " + self.message + ", Image: " + self.image_file + "]\n"
        return prnt
