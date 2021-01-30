import json

from inventar import Inventar, Lizh, Sanki, Bord, Helmet, Restorer


class Baza:
    def __init__(self, name):
        self.name = name
        self._inventar = []
        self.money = 0

    def add_inventar(self, type_inv: Inventar):
        if isinstance(type_inv, Inventar) and type_inv.owner is None:
            type_inv.owner = self
            self._inventar.append(type_inv)
        else:
            raise ValueError

    def save(self):
        with open(f'{self.name}_inventar.json', 'w') as file:
            json.dump([exemp.data for exemp in self._inventar], file)

    def restore(self):
        with open(f'{self.name}_inventar.json', 'r') as file:
            result = json.load(file)
            for item in result:
                exemplyar = Restorer.restore(item)
                self.add_inventar(exemplyar)

    def arenda(self, invent: Inventar):
        if invent in self._inventar:
            self.money += invent.cost
            self._inventar.pop(self._inventar.index(invent))

    def vozvrat(self, invent: Inventar):
        self._inventar.append(invent)

    def __str__(self):
        return f'{self._inventar}'


class Podemnik:
    VOZMOJNUE_VARIANTU = [(Lizh, Helmet), (Sanki), (Bord, Helmet)]

    @staticmethod
    def check_inventar_of_person(inventar):
        for i in Podemnik.VOZMOJNUE_VARIANTU:
            if all(map(lambda x: isinstance(x, i), inventar)):
                return True
            else:
                raise ValueError('ей ты что-то забыл')

    # @staticmethod
    # def check_inventar_of_person(inventar):
    #     if any(map(lambda x: isinstance(x, Lizh), inventar)):
    #         if any(map(lambda x: isinstance(x, Helmet), inventar)):
    #             return True
    #     if any(map(lambda x: isinstance(x, Bord), inventar)):
    #         if any(map(lambda x: isinstance(x, Helmet), inventar)):
    #             return True
    #     if any(map(lambda x: isinstance(x, Sanki), inventar)):
    #         return True
    #     else:
    #         raise ValueError('ей ты что-то забыл')

    @staticmethod
    def ride(person: 'Person'):
        if Podemnik.check_inventar_of_person(person.inventar):
            for example in person.inventar:
                example.use()

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(Podemnik.VOZMOJNUE_VARIANTU):
            raise StopIteration
        y = Podemnik.VOZMOJNUE_VARIANTU[self.index]
        self.index += 1
        return y

class Person:

    def __init__(self, name, money):
        self.name = name
        self.__inventar = []
        self._money = money

    @property
    def inventar(self):
        return self.__inventar

    def take_inventar(self, baza: Baza, inventar: Inventar):
        if inventar in baza._inventar:
            baza.arenda(inventar)
            self._money -= inventar.cost
            self.inventar.append(inventar)
        else:
            raise ValueError('такой икиперовки нету ')

    def retern_inventar(self, baza: Baza, inv_: Inventar):
        if inv_ in self.inventar:
            baza.vozvrat(inv_)
            self.inventar.pop(self.inventar.index(inv_))
        else:
            raise ValueError('что-то пошло не так ')

    @property
    def money(self):
        return self._money

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.inventar):
            raise StopIteration
        x = self.inventar[self.index]
        self.index += 1
        return x


if __name__ == '__main__':
    p1 = Person('ivan', 3000)
    b1 = Baza('Bukovel')
    l1 = Lizh(343)
    l2 = Helmet(323)
    h2 = Helmet(434)
    bo2 = Bord(322)
    b1.add_inventar(l1)
    b1.add_inventar(l2)
    b1.add_inventar(bo2)
    b1.add_inventar(h2)


    print(b1.__dict__)
    p1.take_inventar(b1, l1)
    p1.take_inventar(b1, l2)
    Podemnik.ride(p1)
    print(p1.__dict__)
    p2 = Person('vasul', 1000)
    p2.take_inventar(b1,bo2)
    p2.take_inventar(b1,h2)
    Podemnik.ride(p2)
    p2.retern_inventar(b1,h2)

    print(p2.__dict__)




