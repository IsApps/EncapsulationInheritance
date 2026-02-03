class Wallet:
    def __init__(self, balance,):
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
        
    def set_balance(self, balance):
        if 0 <= balance:
            self.__balance = balance
        else:
            print("Error: Balance cannot be less than zero")

balance1 = Wallet(1000)
balance2 = Wallet(-2)

print(balance1.get_balance())
print(balance2.get_balance())


        
