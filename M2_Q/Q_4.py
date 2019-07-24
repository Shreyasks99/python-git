#4.	Write a program to accept an input string from the user and determine the vowels in the string and calculate the number of vowels. #
import random as random
names= input("Enter your name:")
lst=['a','e','i','o','u']
for name in names:
        if name in 'aeiou':
                print(name)
print(len(list(filter(lambda x:x in lst,names))))

