'''не связано  мнежду собой '''


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def workers_add(self):
        return self.workers

    @workers_add.setter
    def workers_add(self, v):
        if v not in self.workers:
            self.workers.append(v)

    def __repr__(self):
        return (f'{self.id}, {self.name} , {self.company}')

    def __str__(self):
        return (f'{self.id}, {self.name} , {self.company}')


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss = None):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = boss

    @property
    def myboss(self):
        return self.__boss

    @myboss.setter
    def myboss(self, boss: Boss):
        self.__boss = boss

    def __repr__(self):
        return (f'{self.id}, {self.name} , {self.company}, {self.__boss}')

    def __str__(self):
        return (f'{self.id}, {self.name} , {self.company},{self.__boss}')


if __name__ == "__main__":
    a = Boss(43, 'fdf', 'alyans')
    e = Boss(41, 'name', 'com')
    b = Worker(5435, 'ivan', 'рога и  копита')
    c = Worker(142132, 'tolya', 'papa karlo')

    a.workers_add = b
    e.workers_add = c
    b.myboss = a

    print(a.__dict__)
    print(b.__dict__)
    print(e.__dict__)
