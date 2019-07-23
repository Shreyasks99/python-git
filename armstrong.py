
def armstrong_num(num):
    num_1=num
    res=0
    while num != 0:
        r = num%10
        res = res + r ** 3
        num = num//10
    
    return num_1 == res

num=int(input("Enter the number:"))
if armstrong_num(num):
    print(f"Given number {num} is an armstrong number")
else:
    print(f"Given number {num} is not an armstrong number")
