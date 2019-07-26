from Q_15 import Name

class Name_1:
    name = []

    @classmethod
    def addInfo(cls):
        accno = input("Enter the accno:")
        name = input("Enter the name:")
        balance = input("Enter the balance:")
        cls.name.append(Name(accno,name,balance))
