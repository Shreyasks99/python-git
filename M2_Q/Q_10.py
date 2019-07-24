'''10.	Write a program to count the number of unique words and the number of occurrences of each of those words from the question provided below.
Input:
"How much wood would a woodchuck chuck if the woodchuck could chuck wood?"
Output:
Number of unique words: x
abcd: p times
efgh: q times
rstu: t times
……
(Where abcd, efgh and stuv are words from the given input question; p, q and t are the number of instances these words appear in the input.)
'''

names =input("Enter the sentence")
data = names.split(" ")
unique = []

list_1 = {}
for word in data:
    if not word in list_1:
        list_1[word] = 1
    else:
        list_1[word] +=1

for word_1 in list_1:
    if list_1[word_1] == 1:
        unique.append(word_1)
        print(f"{word_1} : {list_1[word_1]}")

print(f"Unique word length is",len(unique))

