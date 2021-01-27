class MyClass:

    def __init__(self, *args):
        self.args = args


    def __getitem__(self, item):
        if 0 <= item < len(self.args):
            return self.args[item]
        raise ValueError ( 'нету такого ')


    def __iter__(self):
        print('call')
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.args):

            raise StopIteration
        lena = self.args[self.index]
        self.index += 1
        return  lena


if __name__ == '__main__':

    b = MyClass(1,2,3,"432", 433, {1,2,3})
    for i in b:
        print(i)

    print(b[1])





