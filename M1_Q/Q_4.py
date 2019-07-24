#4.	Write a program to accept a number “n” from the user; then display the sum of the following series:1/23 + 1/33 + 1/43 + …… + 1/n3#
import math
n=int(input("Enter the number:"))
sum=1
for i in range(2,n+1):
    sum+=1/math.pow(i,3)
print(f"Sum of series={sum}")