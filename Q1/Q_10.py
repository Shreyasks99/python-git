#10.	Write a program to print the following output pattern.#
num=int(input("Enter the number:"))
for i in range(1,num+1):
    for j in range(num,i-1,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")

    for l in range(k-1,0,1):
        print(l,end=" ")
        print()
        
