#5.	Write a program to print the Fibonacci series up to the number 34. (Example: 0, 1, 1, 2, 3, 5, 8, 13, … The Fibonacci Series always starts with 0 and 1, the numbers that follow are arrived at by adding the 2 previous numbers.)#
def fibinocci(n):
    a=0
    b=1
    if n<0:
        print("Incorrect input")
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return b
n=int(input("Enter the value of n"))
print(fibinocci(n))


