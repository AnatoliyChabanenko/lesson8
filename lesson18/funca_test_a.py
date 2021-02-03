import sys
import tempfile
import unittest

from funca import PhoneBook


class TestPhoneBook(unittest.TestCase):
    def setUp(self) -> None:
        self.__fn = tempfile.mktemp()
        self.__firstname = "Igor"
        self.__phone = '123123123'
        self.__addr = '12da asdfa sdf'
        self._okline = f'{self.__firstname},{self.__phone},{self.__addr}'
        self.__badline ='asda.das.d'

    def test_create(self):
        pb = PhoneBook(self.__fn)
        self.assertTrue(pb.contact == [])

    def test_add_rec(self):
        pb = PhoneBook(self.__fn)
        pb.add_contact({'1':'111'})
        self.assertTrue(len(pb.contact))

    def test_add_rec_fail(self):
        pb = PhoneBook(self.__fn)
        self.assertRaises(Exception, pb.add_contact, 123123)

    def test_create_contact(self):
        pb = PhoneBook(self.__fn)
        contact = pb.create_contact_line(self._okline)
        self.assertEqual(contact.get('firstname'), self.__firstname)
        self.assertEqual(contact.get('phone'), self.__phone)
        self.assertEqual(contact.get('address'), self.__addr)
        self.assertRaises(Exception, pb.create_contact_line, self.__badline)





if __name__ == '__main__':
    print(sys.argv)
    # unittest.main()
    # pb = PhoneBook('123.txt')
    # print(pb.create_contact(firstname="4444"))
