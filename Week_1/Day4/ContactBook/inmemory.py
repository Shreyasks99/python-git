from contact import Contact

from beautifultable import BeautifulTable

class InMemoryImpl:

    contact_list = []

    @classmethod
    def add_contact(cls):
        name = input("Enter the name:")
        email = input("Enter the email:")
        mobile = input("Enter the number:")
        city = input("Enter the address:")
        cls.contact_list.append(Contact(name,email,mobile,city))
        print(f"Contact is successfully added with the name:{name}")

    @classmethod
    def delete_contact(cls):
        if len(cls.contact_list) > 0:
            name = input("Enter the name to be deleted")
            contact = cls.get_contact_by_name(name)
            if contact:
                cls.contact_list.remove(contact)
                print(f"Contact {name} is successfully deleted")
                InMemoryImpl._paint(cls.contact_list)
        else:
            print("Contact book is empty")
                
    
    @classmethod
    def view_contacts(cls):
        InMemoryImpl._paint(cls.contact_list)
    
    @classmethod
    def search(cls):
        if len(cls.contact_list) > 0:
            name = input("Enter the name to be searched:")
            s_list = list(filter(lambda x: name.lower() in x.get__name().lower(),cls.contact_list))
            if len(s_list) > 0:
                InMemoryImpl._paint(s_list)
            else:
                print("No data is found based on the search data")
        else:
            print("Contact book is empty")

    @classmethod
    def update_contact(cls):
        name = input("Enter the name to be updated")
        contact = cls.get_contact_by_name(name)
        if contact:
            ch = int(input("Enter the option to update in contact 1.Name 2.Email 3.Mobile 4.Address"))
            if ch == 1:
                print(f"Old name: {contact.get__name()}") 
                name = input("Enter the new name")
                contact.set__name(name)

            elif ch == 2:
                print(f"Old email: {contact.get__email()}") 
                email= input("Enter the new email")
                contact.set__email(email)
            
            elif ch == 3:
                print(f"Old mobile: {contact.get__mobile()}") 
                mobile= input("Enter the new mobile")
                contact.set__mobile(mobile)

            elif ch == 4:
                print(f"Old address: {contact.get__address()}") 
                address= input("Enter the new address")
                contact.set__address(address)
        else:
            print("Contact book does not contain searched data")

    @staticmethod
    def _paint(lst):
        if len(lst) != 0:
            table = BeautifulTable()
            table.column_headers = ["Name","Email","Mobile","Address"]
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__address()])
            print(table)
        else:
            print(f"Contact book is empty!")

    @classmethod
    def get_contact_by_name(cls , name):

        if len(cls.contact_list) > 0:
            contact = list(filter(lambda x:x.get__name().lower() == name.lower(),cls.contact_list))
        return contact[0] if contact else None