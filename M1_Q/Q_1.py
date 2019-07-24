# 1.Write a program to accept a number and determine whether it is a prime number or not #
import math
def is_prime_fun(num):
    if num < 2:
        return False
    else:
        for i in range(2,num//2 +1):
            if num % i == 0:
                return False
    return True
num=int(input("Enter the number:"))
is_prime=is_prime_fun(num)
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
    