class Account:          # Class - A prototype that defines the caracteristics or the object that wil lbe defined
    def __init__(self, filepath):
        self.filepath = filepath # This is an instance variable, th
        with open(filepath, "r") as file:
            self.balance = int(file.read())

    def withdrow(self, ammount):
        self.balance = self.balance - ammount

    def deposit(self, ammount):
        self.balance = self.balance + ammount

    def commit(self):
        with open(self.filepath, "w") as file:
           file.write(str(self.balance))

class Checking(Account): # Inheritance, creating an child class based on mother class

    type = "checking" # declared outside methods and it's shard by all instances of a class.

    """This class generates checking account objects""" # you call this using object_instance_name.__doc__ and returns the content of brackets
    def __init__(self,filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, ammount):
        self.balance = self.balance - ammount - self.fee


# Instantiation is the process of creating class instances


checking = Checking("balance.txt", 20) # this is an object or object instance/ This is instantiation too

checking.deposit(100)
checking.commit()

print(checking.balance)

