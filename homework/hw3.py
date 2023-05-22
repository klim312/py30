class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = input("Enter the amount you want to add: ")
        self._balance += float(amount)
        print("New balance:", self._balance)

    def _kill(self):
        self._balance = 0

    def _jackpot(self):
        self._balance *= 10

    def _combine_balance(self, other):
        self._balance += other.get_balance()

    def get_balance(self):
        return self._balance



client1 = Bank("klim", 100)
client2 = Bank("beka", 100)

client1.moneyX()
print(client1.get_balance())

client1._jackpot()
print(client1.get_balance())

client1._combine_balance(client2)
print(client1.get_balance())

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.b

    def __sub__(self, other):
        return self.a - other.b

    def __mul__(self, other):
        return self.a * other.b

    def __truediv__(self, other):
        return self.a / other.b


num1 = Calculator(10, 5)
num2 = Calculator(2, 3)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
