#9.	Write a program to find the word(s) that occur maximum and minimum number of times in the given paragraph. Also, display those words next to their respective count.
sentence = input("Enter the sentence:")

list_1 = sentence.strip(" ").split(" ")

list_2 = {}

for word in list_1:
    if not word in list_2:
        list_2[word] = 1
    else:
        list_2[word] += 1


max_1 = max(list_2.values())
min_1 = min(list_2.values())

for a,b in list_2.items():
    if b == max_1 or b == min_1:
        print (f" {a} : {b}")