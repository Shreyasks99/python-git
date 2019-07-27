class Stack:
    def __init__(self):
        self.st = []

    def push(self):
        ele = int(input("Enter the element to be pushed:"))
        self.st.append(ele)
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            ele = self.st.pop(0)
            print(f"Element  {ele} is popped from the stack")

    def search(self):
        s_ele = int(input("Enter the element:"))
        if self.is_empty():
            print("Stack is empty")
        else:
            for i,ele in enumerate(self.st):
                if s_ele == ele:
                    print(f"Element {s_ele} is present at {i}")
                    return            

    def show(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for ele in self.st:
                print(f"{ele}",end = " ")
            print()

    def is_empty(self):
        if len(self.st) == 0:
            print("Stack is empty")

if __name__ == "__main__":
    st = Stack()
    while True:
        print("1.Push 2.Pop 3.Search 4.Display 5.exit")
        try:
            ch = int(input("Enter your choice:"))
            if ch == 1:
                st.push()
            elif ch == 2:
                st.pop()
            elif ch == 3:
                st.search()
            elif ch ==4:
                st.show()
            elif ch == 5:
                break
            else:
                print("Enter numbers only from 1 to 5")

        except (ValueError,KeyError):
            print("Enter the numbers only from 1 to 5")
    