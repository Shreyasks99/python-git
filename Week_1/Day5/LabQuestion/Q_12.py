num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
num_3 = int(input("Enter the third number:"))

def biggest(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(f"Biggest of the three numbers {num1} {num2} and {num3} is:{num1}")
    elif num2 > num3:
         print(f"Biggest of the three numbers {num1} {num2} and {num3} is:{num2}")
    else:
         print(f"Biggest of the three numbers {num1} {num2} and {num3} is:{num3}")

biggest(num_1,num_2,num_3)