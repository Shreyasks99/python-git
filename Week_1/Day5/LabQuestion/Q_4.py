''' Prime Numbers between 2 Bounds '''
def is_prime(num):
    if num < 2:
        return False
    
    else:
        for i in range(2,num//2 +1):
            if num % i == 0:
                return False
        return True
LB = int(input("Enter the lower bound:"))
UB = int(input("Enter the upper bound:"))
for i in range(LB,UB+1):
    if is_prime(i):
        print(i)
