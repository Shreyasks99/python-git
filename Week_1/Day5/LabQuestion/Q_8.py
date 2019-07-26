year = int(input("Enter the year:"))
print(f"Year:{year} is a leap year" if year % 4 == 0 and not year % 100 ==0 or year % 400 == 0 else f"Year:{year} is not a leap year")