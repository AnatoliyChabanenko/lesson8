import json
from typing import List


class PhoneBook:

    MAGIC_TAB = "\t|\t"

    LINE_FORMAT = {
        'firstname': 0,
        'phone': 1,
        'address': 2,
    }

    DEFAULT_DATA = {
        'firstname': '',
        'phone': '',
        'age': 18,
        'address': '-'
    }

    def __init__(self, fn):
        self.__fn = fn
        self.__contacts = []
        self.__load_data()

    @property
    def contact(self):
        return self.__contacts

    def add_contact(self, dat):
        if type(dat) is dict:
            self.__contacts.append(dat)
            self.__store_to_disk()

            # for k in dat:
            #     if k in self.DEFAULT_DATA:
            #         if type(self.DEFAULT_DATA[k]) != type(dat[k]):
            #             raise Exception
            #         else:
            #             self.__contacts.append(dat)
            #             self.__store_to_disk()
            #     else:
            #         raise Exception(f"Не установлено значение ключа {k}")
        else:
            raise Exception

    def __load_data(self):
        try:
            with open(self.__fn, "r") as f:
                self.__contacts = json.load(f)
        except:
            self.__contacts = []

    def __store_to_disk(self):
        pass

    def search(self, key, val) -> List:
        return []

    def delete(self, dat: List):
        pass
        self.__store_to_disk()

    def create_contact_from_line(self, line_in="Igor, +380213123123, Poltava Shevchenko 15 app54"):
        ret = {}
        for k in self.LINE_FORMAT:
            if len(line_in.split(self.MAGIC_TAB, )) >= self.LINE_FORMAT[k] + 1:
                ret[k] = line_in.split(self.MAGIC_TAB, )[self.LINE_FORMAT[k]]
            else:
                ret[k] = self.DEFAULT_DATA[k]
        return ret

    def create_contact_to_line(self, contact) -> str:
        str_contact = ','.join(contact.values())
        return str_contact


if __name__ == '__main__':
    pass