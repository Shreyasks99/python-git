#7.	Write a program to accept a number from the user and determine the sum of digits of that number. Repeat the operation until the sum gets to be a single digit number.
num = int(input("Enter the number"))
sum = 0
while num !=0:
    sum += num%10
    num = num//10
    print(f"Sum of digits:{sum}")

