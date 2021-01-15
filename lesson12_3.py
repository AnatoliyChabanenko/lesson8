from fractions import Fraction
class Fractio :
    def __init__(self , x , y):
        self.x = x
        self.y = y

    def plus(self):
        return Fraction(self.x) + Fraction(self.y)

    def ninus(self):
        return Fraction(self.x) - Fraction(self.y)

    def division(self):
        return Fraction(self.x) / Fraction(self.y)

ads= Fractio('1/5', '1/4')
print(ads.division())