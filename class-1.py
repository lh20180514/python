class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def drink(self):
        print("Energy!")
    def drink(self,how_much):
        if how_much == 'a sip':
            print('Cool')
        elif how_much == 'whole bottle':
            print('Headache!')
    def __init__(self):
        self.test = 'Test'
        for element in self.formula:
            print('Coke has {}!'.format(element))
    def __init__(self, test):
        self.test = test;
        for element in self.formula:
            print('Coke has {}!'.format(element))

coke_for_me = CocaCola('可口可乐test')
print(coke_for_me.formula)
print(CocaCola.formula)

# 新增类的属性
CocaCola.local_logo = '可口可乐'
print(CocaCola.local_logo)

coke = CocaCola('可口可乐test')
coke.drink('a sip')

print(CocaCola('可口可乐test').test)