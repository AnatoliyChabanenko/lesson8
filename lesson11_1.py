
class Person:
    def name(self):
        return 'humman '
class Student(Person):
    def car (self):
        return 'BMW'

class Teacher (Student):
    def sallery(self):
       return 1000

x1 = Teacher()
print((x1.name()))
print(x1.car())