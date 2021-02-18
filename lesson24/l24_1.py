from lesson24.l24_2 import Node


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count


    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        current = self._head
        temp = Node(item)
        if current:
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(temp)
        else:
            self._head = temp

    def insert(self, index, item):
        current = self._head
        for i in range(index):
            current = current.get_next()

        if current != None:
            temp = Node(item)
            temp.set_next(current.get_next())
            current.set_next(temp)
        else:
            raise ("index out of range")


    def pop(self):
        current = self._head
        previous = None

        if current == None:
            return "No item in list"
        while current.get_next() != None:
            previous = current
            current = current.get_next()

        previous.set_next(None)
        return current.get_data()

    def index(self, item):
        current = self._head
        found = False
        index = 0

        while current != None and not found:
            if current.get_data() != item:
                index += 1
                current = current.get_next()
            else:
                found = True

        if found:
            return index
        else:
            return "Not Found"

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))
    print(my_list)

    my_list.append(44)
    print(my_list.index(44))
    print(my_list)
    my_list.pop()
    print(my_list)

