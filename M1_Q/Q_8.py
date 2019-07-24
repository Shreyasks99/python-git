#8.	Write a program to accept 2 numbers “m” and “n” from the user; determine the value of mn without using predefined functions.#
m=int(input("Enter the value of m:"))
n=int(input("Enter the value of n:"))
sum=1
for i in range(0,n):
    sum=sum*m
print(f"m^n={sum}")