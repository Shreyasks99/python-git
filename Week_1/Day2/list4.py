lst=[]
def add(ele):
    lst.append(ele)
    return

def pop():
    if len(lst) == 0:
        print("No element to be deleted")
    ele=lst.pop()
    print(f"Popped element is {ele}")
    return

def search(ele):
    for ele in lst:
        print("Element is present")
        return
    print("Element is not present")
    return

def display():
    if len(lst) == 0:
        print("No element to be displayed")
    print(lst)
    return

while True:
    print("**** 1.Add 2.Delete 3.Search 4.Display 5.Exit")
    ch=int(input("Enter the operation:"))
    if ch == 1:
        ele=int(input("Enter the element to be added:"))
        add(ele)
    elif ch == 2:
        pop()
    elif ch == 3:
        sea=int(input("Enter the element to be searched:"))
        search(sea)
    elif ch == 4:
        display()
    else:
        print("Exited from the operation")
        break



    