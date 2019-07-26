num = int(input("Enter the number"))
num_1 =0
count =1
while True:
    if num == 0:
        break
    temp = num % 10
    num = num//10
    if temp == 9:
        temp = 0
    else:
        temp = temp + 1
    num_1= num_1 + (temp*count)
    count = count * 10
print(num_1)