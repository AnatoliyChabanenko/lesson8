'''TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
 if the channel N or 'name' exists in the list, or "No" - in the other case.

    def first_channel(self):
        self.

'''
CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:

    def __init__(self, CHANNELS , new_chenal = 0 ):
        self.CHANNELS = CHANNELS
        self.new_chenal= new_chenal

    def first_channel(self):
        self.new_chenal = 0
        return self.CHANNELS[self.new_chenal]

    def last_channel(self):
        self.new_chenal = -1
        return self.CHANNELS [self.new_chenal]

    def turn_channel(self, N):
        self.N = N - 1
        return self.CHANNELS[self.N]

    def next_channel(self):
        self.new_chenal += 1
        return self.CHANNELS[self.new_chenal]

controller = TVController(CHANNELS)
print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(2))
print(controller.next_channel())
