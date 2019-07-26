''' Sum f Digits '''
num = int(input("Enter the number"))
temp = num
sum = 0
while num > 9:
    sum = (num % 10 + num //10)
    num = sum
print(f"Sum of {temp} is {sum}")
