'''2.	Write a program to accept a two-dimensional array containing integers as the parameter and determine the following from the elements of the array:
a.	element with minimum value in the entire array
b.	element with maximum value in the entire array
c.	the elements with minimum and maximum values in each column
d.	the elements with minimum and maximum values in each row'''

num = [[0,1,2,3],[3,4,5,5],[6,7,8,8],[9,0,1,9]]
for i in num:
    print(f"Max in each row:{max(i)} Min in each row:{min(i)}")
nums =[j for i in num for j in i]
print(f"Maximum in whole array:{max(nums)} Minimum in whole array:{min(nums)}")




