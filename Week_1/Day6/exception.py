try: 
    num1 = int(input("Enter the number1:"))
    num2 = int(input("Enter the number2:"))
    print(num1 ** num2)
    print(num1 / num2)
    print("Sum is:" +(num1+num2))
except ZeroDivisionError:
    print("Division by zero not possible")
except ValueError:
    print("Please enter only zeros")
except Exception as e:
    print(f"Somethingwent wrong {e}")
