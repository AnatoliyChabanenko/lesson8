class Product:
    def __init__(self, gr='', name='', price=0):
        self.group = gr
        self.name = name
        self.price = price

    def myhash(self):
        return f"{self.name}{self.group}"


class ShopProduct:
    nacenka = 5

    def __init__(self, prod: Product):
        self.prod = prod
        self.price = prod.price

    def new_price(self, p):
        self.price = p

    def set_discount_name(self, percent, prod2):
        self.prod_prise = prod2
        self.percent = percent
        if not isinstance(percent, (int, float)):
            raise ValueError('процент пожалуста циферками ')
        for self.prod_prise in self.prod.name:
            self.prod.price -= self.percent

    def set_discount(self, p):
        self.price -= self.price * (p / 100)
        self.price = max(self.price, self.prod.price)

    def current_price(self):
        return max(self.prod.price * (1 + self.nacenka / 100), self.price)


class ProductStore:
    def __init__(self):
        self.earned_money = 0
        self.data = {}

    def add(self, prod, qty):
        my_prod = ShopProduct(prod)
        if qty <= 0:
            return
        if my_prod in self.data:
            self.data[my_prod] += qty
        else:
            self.data[my_prod] = qty

    def print_data(self):
        return self.data

    def sell(self, name, qty):
        for my_prod in self.data:
            if my_prod.prod == name:
                if self.data[my_prod] >= qty:
                    self.earned_money += my_prod.current_price() * qty
                    self.data[my_prod] -= qty
                    break
        else:
            raise ValueError("Товар не найден")

    def get_income(self):
        return self.earned_money

    def get_all_products(self):
        return print(f'такие товары ребята {self.data}')


if __name__ == '__main__':
    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 150)
    s = ProductStore()
    f = ShopProduct(p2)
    print(p2.price)
    f.set_discount_name(1, 'Ramen')
    print(p2.price)
    s.add(p, 10)
    s.sell(p, 9)
    s.get_all_products()
    print(s.earned_money)
