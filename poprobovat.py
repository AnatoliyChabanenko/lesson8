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
        if invent.owner is self:
            self._inventar.append(invent)
        raise ValueError('это инвентарь не той бази')

    def __str__(self):
        return f'{self._inventar}'


class Podemnik:
    VOZMOJNUE_VARIANTU = [[Lizh, Helmet], [Sanki], [Bord, Helmet]]

    @staticmethod
    def check_inventar_of_person(inventar):
        if any(map(lambda x: isinstance(x, Lizh), inventar)):
            if any(map(lambda x: isinstance(x, Helmet), inventar)):
                return True
        if any(map(lambda x: isinstance(x, Bord), inventar)):
            if any(map(lambda x: isinstance(x, Helmet), inventar)):
                return True
        if any(map(lambda x: isinstance(x, Sanki), inventar)):
            return True

        else:
            raise ValueError('ей ты что-то забыл')

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
        self.money = money

    @property
    def inventar(self):
        return self.__inventar

    def take_inventar(self, baza: Baza, inventar: Inventar):
        if inventar in baza._inventar:
            baza.arenda(inventar)
            self.money -= inventar.cost
            self.inventar.append(inventar)
        else:
            raise ValueError('такой икиперовки нету ')

    def retern_inventar(self, baza: Baza, inv_: Inventar):
        if inv_ in self.inventar:
            baza.vozvrat(inv_)
            self.inventar.pop(self.inventar.index(inv_))
        else:
            raise ValueError('что-то пошло не так ')

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
    p1 = Person('Vasul', 3000)
    p2 = Person('igor', 1000)
    l1 = Lizh(300)
    l2 = Lizh(200)
    l3 = Lizh(400)
    h1 = Helmet(200)
    a = Baza('bukovel')
    a1 = Baza('Bukovel2 ')
    a.add_inventar(h1)
    a.add_inventar(l1)
    p1.take_inventar(a, h1)
    p1.take_inventar(a, l1)
    Podemnik.ride(p1)
    p1.retern_inventar(a, l1)
    print(h1.__dict__)
    print(a1.__dict__)
    print(a.__dict__)
    print(l1.__dict__)
    print(p1.__dict__)

