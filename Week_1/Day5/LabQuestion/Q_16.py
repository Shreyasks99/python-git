def q_feature(list_1):
    if name.endswith("?"):
        print("It is an Interrogation Sentence")
    else:
        print("It is an assertive sentence")

while True:
    print("1.Enter 2.Exit")
    ch = int(input("Enter the choice:"))
    if ch == 1:
        name = input("Enter the sentence:")
        q_feature(name)
    else:
        break