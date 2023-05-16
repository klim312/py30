# инкапсуляция
# публичный доступ
# защищенный\приватный
# скрытый
class Bank:
    def __init__(self, user, money, key):
        self._user = user
        self.money = money
        self.__key = key

    def set_key(self):
        return self.__key

    def get_key(self, k):
        self.__key = k

    def key(self):
        self._keys()

    def _keys(self):
        print(self.__key)

    def __str__(self):
        return f"name is {self._user}\n" \
               f"money is {self.money}\n" \
               f"key in #####"


k = Bank('beka', 10000000, '12qwer65tre')

print(k.set_key())
k.get_key('9')
print(k.set_key())
# k._user = 'Mirlan'
# k.age = 19
# # k.__key = '111111111111'
# k._Bank__key = '1111111'
# k.key()
#
# print(dir(k))