from inventar import Inventar, Lizh, Sanki, Bord, Helmet


class Baza:
    def __init__(self, name):
        self.name = name
        self.__inventar = []
        self.money = 0

    def add_inventar(self, type_inv: Inventar):
        if isinstance(type_inv, Inventar) and type_inv.owner is None:
            type_inv.owner = self
            self.__inventar.append(type_inv)
        else:
            raise ValueError

    @property
    def baze_inventar(self):
        return self.__inventar

    def arenda(self, invent : Inventar):
        if invent in self.__inventar:
            self.money += invent.cost
            self.__inventar.pop(self.__inventar.index(invent))

    def vozvrat(self, invent : Inventar):
        # if invent.owner == self.name:
        self.__inventar.append(invent)
        # raise ValueError ('это инвентарь не той бази')



class Person:
    def __init__(self, name , money):
        self.name = name
        self.p_inventar = []
        self.money = money

    def take_inventar(self, baza: Baza, inventar: Inventar):
        if inventar in baza.baze_inventar:
            baza.arenda(inventar)
            self.money -= inventar.cost
            self.p_inventar.append(inventar)
        else:
            raise ValueError ('такой икиперовки нету ')

    def retern_inventar(self , baza: Baza , inv_ :Inventar):
        if inv_ in self.p_inventar:
            baza.vozvrat(inv_)
            self.p_inventar.pop(self.p_inventar.index(inv_))
        else:
            raise ValueError ('что-то пошло не так ')

class Podemnik:
    def __init__(self , name , money ):
        self.neme = name
        self.money = money

    def pokatatsa(self , chelovek:Person , invent : Inventar ):
        pass




if __name__ == '__main__':
    a = Baza('bukovel_1')
    l_1 = Lizh(499)
    s_1 = Sanki(32)
    h_1 = Helmet(300)
    b_1 = Bord(700)
    l_2 = Lizh(312)
    a.add_inventar(l_1)
    a.add_inventar(b_1)
    a.add_inventar(h_1)
    a.add_inventar(l_2)
    p_1 = Person('vadim', 3000)
    p_1.take_inventar(a , h_1)
    p_1.take_inventar(a, l_1)
    p_1.retern_inventar(a,l_1)
    p_1.take_inventar(a,l_1)
    p_2= Person('asia',99999)
    p_2.take_inventar(a,l_2)
    p_2.take_inventar(a,b_1)
    p_2.retern_inventar(a,b_1)



    print(p_1.__dict__)
    print(a.__dict__)
    print(l_1.__dict__)

