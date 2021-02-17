

class Stack():

    def __init__(self ):
        self.my= []

    def push(self,item ):
        self.my.append(item)

    def popi(self):
        if self.my != []:
            self.my.pop()
        else:
            raise ValueError ('Empty Steck')

    def red_stack(self):
        for i in self.my:
            print(i[::-1])

    def is_empty(self):
        if self.my != []:
            return False
        else:
            return True

    def get_from_stack(self,element):
        my_list = self.my
        if len(self.my) > element:
            return my_list.pop(element)
        else:
            raise ValueError (' что-то')




if __name__ == '__main__':
    s = Stack()
    s.push('dog')
    s.push('cat')
    s.push('pig')
    s.popi()
    print(s.get_from_stack(2))
