#3.Write a program to accept 2 different numbers from the user and print all the prime numbers between these 2 numbers.#
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
            if n%i==0:
                return False
    return True
LB=int(input("Enter the lower bound:"))
UB=int(input("Enter the upper bound:"))
for i in range(LB,UB+1):
    if is_prime(i):
        print(i)
