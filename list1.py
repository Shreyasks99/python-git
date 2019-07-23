import random as random
lst=[]
for i in range(1,21):
    lst.append(random.randint(1,50))

print(lst)
print("Max:",max(lst))
print("Min:",min(lst))