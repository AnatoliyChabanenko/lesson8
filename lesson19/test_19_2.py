from lesson19 import lesson19_2
import unittest

def vuzov(dat):
    with lesson19_2.FileManager('txt1.txt', 'r') as f:
        f.write(dat)


class Test_my_class(unittest.TestCase):

    def setUp(self) -> None:
        self.test_fail_manader = lesson19_2.FileManager('test_12.txt', 'r')
        self.file_name = 'test_12.txt'
        self.file_mode = 'r'


    def test_create(self):
        test_faile_manader = lesson19_2.FileManager(self.file_name, self.file_mode)
        self.assertEqual(test_faile_manader.filename,self.file_name)
        self.assertEqual(test_faile_manader.mode, self.file_mode)

    def test_create_faild(self):
        test_faile_manader = lesson19_2.FileManager(self.file_name, self.file_mode)
        self.assertEqual(test_faile_manader.filename, self.file_name)
        self.assertEqual(test_faile_manader.mode, self.file_mode)

    def test_1(self):
        with self.assertRaises(FileNotFoundError ,):
            vuzov('3213213')



if __name__ == '__main__':
    unittest.main()

