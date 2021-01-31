import unittest
from lesson17 import lesson15_2

class BossTestCase(unittest.TestCase):

    def setUp(self):
        self.test_boss = lesson15_2.Boss(333,'vitalya', 'alyans')


class PersonTestCase(unittest.TestCase):

    BOSS = lesson15_2.Boss(322, 'bandit', 'рога и копита ')

    def setUp(self) :
        self.w_worker = lesson15_2.Worker(4324, 'vova','unit')


    def test_nowuy_boss(self):
        self.assertEqual(self.w_worker.boss, None)
        self.w_worker.nowuy_boss('bandit')
        self.assertEqual(self.w_worker.boss, 'bandit')

    def test_idy_na_roboty(self):
        self.w_worker.idy_na_roboty(self.BOSS)
        self.assertEqual(self.w_worker.boss , self.BOSS)
        self.assertEqual(self.w_worker.company , self.BOSS.company)

    def test_idy_z_zoboty(self):
        self.w_worker.idy_z_zoboty(self.BOSS)
        self.assertEqual(self.w_worker.boss , None)


if __name__ == '__main__':
    # PersonTestCase.BOSS = lesson15_2.Boss()
    unittest.main()
