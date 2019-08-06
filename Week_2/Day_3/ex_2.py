import re

data = "Learning- Python, is fun. Python_programming is, easy"
lst = re.sub(r"-|,|_"," ",data)
print(lst)