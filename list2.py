import random as random
lst=[]
list=[]
for i in range(1,101):
    lst.append(random.randint(1,1000))
print(lst)

for ele in range(1,101):
    if ele % 3 ==0 and ele % 6 ==0 and not ele % 9 == 0:
            list.append(ele)
print(list)
            