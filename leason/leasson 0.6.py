# ООП - обьектно ориентированное программирование

# что такое класс

# полиморфизм наследование инкапсуляция

class A:
    a = 1

    # маг метод
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def run(self):
        print(self.a, 'run')


o = A('a', 'b')
o1 = A('Beka', 'bekbolsun')


# o.run()


class B(A):
    def abab(self):
        super().run()
        self.run()

    def run(self):
        print('я новый метод')


p = B('a', 'b')
# p.run()
p.abab()


class B1:
    def __init__(self, b1):
        self.b1 = b1


print(B.mro())


class C(B, B1, A):
    def __init__(self, a, b, b1):
        A.__init__(self, a, b)
        B1.__init__(self, b1)


c = C('1', 1, 0)
# MRO-