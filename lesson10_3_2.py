CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.next_number = 0

    def first_channel(self):
        self.next_number = 0
        return self.current_channel()

    def last_channel(self):
        self.next_number = -1
        return self.current_channel()

    def turn_channel(self, N):
        self.next_number=self.N = N - 1
        return self.channels[self.N]

    def next_channel (self):
        if self.next_number != len(self.channels)-1:
            self.next_number += 1
        else:
            self.next_number = 0
        return self.current_channel()

    def previous_channel(self):
        if self.next_number != 0:
            self.next_number -= 1
        else:
            self.next_number = len(self.channels)-1

    def current_channel(self):
        return self.channels[self.next_number]

    def is_exist(self, name):
        self.name = name
        if name in self.channels:
            return 'Yes'
        else:
            return 'no'

controller = TVController(CHANNELS)
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist('BBC'))