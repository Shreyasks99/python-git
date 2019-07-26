from inmemory import InMemoryImpl

while True:
    print("*"*80)
    print("1.Add Contact 2.Delete Contact 3.View All 4.Search Contact 5.Update Contact 6.Exit")
    print("*"*80)
    ch = int(input("Enter your choice:"))
    if ch == 1:
        InMemoryImpl.add_contact()
    elif ch == 2:
        InMemoryImpl.delete_contact()
    elif ch == 3:
        InMemoryImpl.view_contacts()
    elif ch == 4:
        InMemoryImpl.search()
    elif ch == 5:
        InMemoryImpl.update_contact()
    else:
        break
