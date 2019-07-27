def searchEle(lst,ele):
    index = -1
    for i in lst:
        index +=1
        if i == ele:
            return index
    return -1

def binarySearch(lst,key):
    l=0
    h=len(lst) -1
    while l <= h:
        mid = (l + h) //2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            l = mid + 1
        else:
            h = mid + 1
    return -1

def bubbleSort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]

'''l = [9,8,7,6]
bubbleSort(l)
print(l)'''
ele = 8
res = binarySearch([1,2,3,4,5,6,7,8],ele)
if not res == -1:
    print(f"Element is present at location")
else:
    print(f"Element is not present")


'''ele = 6
res = searchEle([1,2,3,4,5,6],ele)
if res == -1:
    print("Element is not present")
else:
    print(f"Element {ele} is present at {res} location")
'''