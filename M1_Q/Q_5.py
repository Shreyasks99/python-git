#5.	Write a program to print the Fibonacci series up to the number 34. (Example: 0, 1, 1, 2, 3, 5, 8, 13, … The Fibonacci Series always starts with 0 and 1, the numbers that follow are arrived at by adding the 2 previous numbers.)#
a=0
b=1
c=0
print(a,b,end = " ")
while not c == 34:
    c=a+b
    print(c,end = " ")
    a,b=b,c