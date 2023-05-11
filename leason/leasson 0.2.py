class People:
    a = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f"{self.name} run")

    def __str__(self):
        return f"{self.name},{self.age}"


a = People('beka', 17)
print(a.age)
a.run()
print(a)


# наследование полиморфизм

class Student(People):
    def __init__(self, name, age, homew):
        super().__init__(name, age)
        # People.__init__(self,name,age)
        self.home = homew

    def eating(self):
        print(f"{self.name} eating")

    def run(self):
        print(f'{self.name} flying')


aza = Student('Aza', 18,False)
# aza.eating()
# aza.run()
# print(aza)
print('#############')
People.run(aza)
