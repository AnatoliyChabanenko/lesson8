'''Створіть базовий клас з іменем Animal за допомогою методу,
 який називається talk, а потім створіть два підкласи:
  Dog і Cat та створіть власну реалізацію методу talk. Наприклад,
  Dog's може друкувати "woof woof", тоді як
  Cat's може друкувати "мяу".
  Крім того, створіть просту загальну функцію,
  яка бере як вхідний екземпляр класів Cat або Dog і
  виконує метод обговорення щодо вхідного параметра.
'''

class Animal:
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        return 'мяу'

class Dog (Animal):
    def talk(self):
        return 'woof woof'

def animal_talk(animal):
    print(animal.talk())

cat = Cat()
dog = Dog()
animal_talk(cat)
animal_talk(dog)