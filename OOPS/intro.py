# Instance variable and methods
'''
class Dog:
    ##Contructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
    

#create objects
dog1=Dog("Buddy",3)
print(dog1)
print(dog1.name)
print(dog1.age)



# class with INSTANCE methods

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def is_barking(self):
        print(f"{self.name} says woof")
        
dog1=Dog('buddy',3)
dog1.is_barking()
dog2=Dog('lucy',4)
dog2.is_barking()
'''

# Modeling a Bank account

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"Amount {amount} is deposited. New balance is {self.balance}")
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance.")
        else:
            self.balance-=amount
            print(f"Amount {amount} is withdrawn. New balance is {self.balance}")
        
    def get_balance(self):
        print(f"Current balance is: {self.balance}")

account1=BankAccount("swati")
account1.deposit(300)
account1.withdraw(100)
account1.get_balance()
        