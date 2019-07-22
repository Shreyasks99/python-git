# Write a program to accept a number from the user#
num=int(input("Enter a number:"))
temp=num
rev=0
while num!=0:
        rev=rev * 10 +num % 10
        num //=10

print(f"Reverse of {temp} is {rev}")