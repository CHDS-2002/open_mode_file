import os

os.system('COLOR B')


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self, __file_name='products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        with open(self.__file_name, 'r') as f:
            return ''.join(f.readlines())

    def add(self, *products):
        lines = []

        try:
            with open(self.__file_name, 'r+') as f:
                lines = ''.join(f.readlines()).split('\n')
        except:
            lines = []

        with open(self.__file_name, 'a+') as f:
            for p in products:
                if str(p) in lines:
                    print(f'Продукт {p.name} уже был в магазине, его общий вес теперь равен {p.weight}.')
                else:
                    f.write(f'{str(p)}\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# os.remove('products.txt')

try:
    os.system('PAUSE')
except:
    os.system('CLS')
