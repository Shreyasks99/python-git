# 8.	Write a function which implements the Pascal's triangle.
n = int(input("Enter the number of Rows"))
a = []
for i in range(n):
    a[i].append(1)
    for j in range(1,i):
        a[j].append(a[i-1][j-1] + a[i-1][j])

    if n!=0:
        a[i].append(1)

    for i in range(n):
        
        for j in range(1,i+1):
    
