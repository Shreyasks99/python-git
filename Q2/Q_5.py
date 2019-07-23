#5.	Write a program to add the elements of 2 arrays that are of the same dimension. (Hint: Use map method.)#
list_1=[2,3,4,5]
list_2=[2,1,3,4]
res=list(map(lambda x,y:x+y,list_1,list_2))
print(res)