class Mathematician:
    def __init__(self, mylist):
        self.mylist = mylist
    def square_nums(self):
        return [i**2 for i in self.mylist]
    def remove_positives(self):
        mylist_2= []
        for i in self.mylist:
            if i >= 0:
                mylist_2.append(i)
        return mylist_2
    def filter_leaps(self):
        mysupr_lis = []
        for i in self.mylist:
            if i %4 ==0:
                mysupr_lis.append(i)
        return mysupr_lis
m = Mathematician([2001, 1884, 1995, 2003, 2020])
print(m.square_nums())
print(m.remove_positives())
print(m.filter_leaps())




#
#
# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
#
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
#
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
#
