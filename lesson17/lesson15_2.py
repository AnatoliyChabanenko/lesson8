class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []



    def workers_ad(self, worker : 'Worker'):
        self._workers.append(worker)

    def robotnik_poshol(self , worker : 'Worker'):
        self._workers.remove(worker)
        return print(f' пошол з роботы {worker}')

    def __repr__(self):
        return (f'{self.id}, {self.name} , {self.company}')

    def __str__(self):
        return (f'{self.id}, {self.name} , {self.company}')


class Worker:

    def __init__(self, id_: int, name: str, company = None, boss = None) :
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss


    def nowuy_boss(self , name ):
        self.boss = name



    def idy_na_roboty(self, boss : Boss):
        if isinstance(boss, Boss):
            boss.workers_ad(self)
            self.company = boss.company
            self.boss = boss

    def idy_z_zoboty(self , boss : Boss):
        # boss.robotnik_poshol(self)
        self.company = None
        self.boss = None




    def __repr__(self):
        return (f'{self.id}, {self.name} , {self.company}, {self.boss}')

    def __str__(self):
        return (f'{self.id}, {self.name} , {self.company},{self.boss}')


if __name__ == "__main__":
    a = Boss(43, 'fdf', 'alyans')
    e = Boss(41, 'name', 'com')
    b = Worker(5435, 'ivan', 'рога и  копита')
    c = Worker(142132, 'tolya', 'papa karlo')
    b.idy_na_roboty(a)



    print(a.__dict__)
    print(b.__dict__)
    print(e.__dict__)
