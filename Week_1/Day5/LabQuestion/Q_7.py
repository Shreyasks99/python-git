def is_divisible(num):
    if num == 0:
        return False
    else:
        if num % 9 ==0 and  not num % 5 == 0:
            return True
LB = int(input("Enter the lower bound:"))
UB = int(input("Enter the upper bound:"))
for i in range(LB,UB + 1):
    if is_divisible(i):
        print(i,end = " ")
