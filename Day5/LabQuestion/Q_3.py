''' Sum f Digits '''
num = int(input("Enter the number"))
temp = num
sum = 0
while num!=0:
    sum += num % 10
    num=num//10
if sum > 9:
    sum = 
print(f"Sum of {temp} is {sum}")
