import re

data = "Lakshman and Amalraj are good friends, Arjun and Aruna also are also friends with Anu"
lst = re.findall(r'\bA[a-z]{4,}',data)
print(lst)