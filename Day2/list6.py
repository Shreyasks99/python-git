import random as random
nums = [ random.randint(100,500) for i in range(0,100)]
lst =[]
for ele in nums:
    if ele % 5 == 0:
        lst.append(ele)
print(lst)