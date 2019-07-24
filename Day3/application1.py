from application import Contact

class ContactBook:
    contacts = []

    @staticmethod
    def addContact():
        name = input("Enter the name")
        email = input("Enter the Email")
        mobile = int(input("Enter the mobile"))
        ContactBook.contacts.append(Contact(name,email,mobile))
        print(f"Contact is added with name:{name}")

    @staticmethod    
    def delContact():
        pass
    
    @staticmethod
    def searchContact():
        pass

    @staticmethod
    def viewAll():
        if .get__name == 0:
            print("Contacts yet to added")
        for contact in ContactBook.contacts:
            print(f"{contact.get__name()} {contact.get__email} {contact.get__mobile}")

    @staticmethod
    def updateContact():
        pass
