num =input("Enter the number:")
temp =  num
while num !=0:
    digit = num % 10
    if digit in [2,3,5,7]:
        count = count + 1
    num = num // 10
print("Number of prime numbers in {temp} is:{count}")
