sentence = input("Enter the sentence:")
list_1 = ['a','e','i','o','u']
for name in sentence:
    if name in list_1:
        sentence = sentence.replace(name," ")
print(sentence)