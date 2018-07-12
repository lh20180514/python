class CocaCola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
            'High Fructose Corn Syrup',
            'Carbonated Water',
            'Phosphoric Acid',
            'Natural Flavors',
            'Caramel Color',
            'Caffeine'
            ]
    def __init__(self,logo_name):
        self.local_logo = logo_name
    def drink(self):
        print('You got {} cal energy!'.format(self.calories))

print(CocaCola('Test').local_logo)

class CaffeineFree(CocaCola):
    calories = 0
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
    ]

coke_a = CaffeineFree('Cocacola-FREE')
coke_a.drink()


class TestA:
    attr = 1
    def __init__(self):
        self.attr = 22
#obj_a = TestA()
obj_b = TestA()
#obj_a.attr = 42
print(obj_b.attr)

print(TestA.__dict__)
print(obj_b.__dict__)



a = 1
b = 'String!'
c = []
d = {}
print(type(a),type(b),type(c),type(4))

import sys
print(sys.path)