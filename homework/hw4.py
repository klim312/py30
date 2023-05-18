class SavingAccount: pass
class CheckingAccount: pass
class BankAccount(SavingAccount, CheckingAccount): pass


class RealEstate: pass


class Stock: pass


class Bond: pass


class Security(Stock, Bond): pass


class InterestBearingitem(BankAccount, SavingAccount, CheckingAccount, Stock, Bond): pass


class asset(BankAccount, SavingAccount, CheckingAccount, RealEstate, Stock, Bond,): pass


class Insurableltem(BankAccount, SavingAccount, CheckingAccount, RealEstate, Stock, Bond): pass
