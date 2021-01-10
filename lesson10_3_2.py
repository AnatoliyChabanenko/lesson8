CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    next_number = 0

    def __init__(self, CHANNELS ):
        self.CHANNELS = CHANNELS

    def first_channel(self):
        TVController.next_number = 0
        return self.CHANNELS[self.next_number]

    def last_channel(self):
        TVController.next_number = -1
        return self.CHANNELS [self.next_number]\

    def turn_channel(self, N):
        TVController.next_number= self.N = N - 1
        return self.CHANNELS[self.N]

    def move_to (self):
        TVController.next_number += 1
        if TVController.next_number == 3:
            return self.CHANNELS[0]
        return self.CHANNELS [self.next_number]

    def previous_channel(self):
        TVController.next_number -= 1
        return self.CHANNELS [self.next_number]

    def current_channel(self):
        return self.CHANNELS [self.next_number]

    def is_exist(self, name):
        self.name = name
        if name in self.CHANNELS:
            return 'Yes'
        else:
            return 'no'

controller = TVController(CHANNELS)
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.move_to())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist('BBC'))