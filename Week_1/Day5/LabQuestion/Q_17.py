sentence = input("Enter the sentence:")
if sentence.endswith("y"):
    sentence = sentence[:len(sentence) - 1] + "ies"
print(sentence)
