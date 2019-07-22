import random as random
num=random.randint(1,6)
count=1
while True:
    n=int(input("Enter the number"))
    if n==num:
        print(f"You guessed in {count} attemptes")
        count+=1
        break
    elif n>num:
        print("Guessed number is greater")
        count+=1
    else:
        print("Number chosen is smaller")

    if count == 3:
        print("lost all your try")
        break
