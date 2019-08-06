'''2.	Write a program to get the all the numbers from the following string:
	“1007 Lakshman 1008 Karthik 1009-Ramesh -1010 Suresh”

Expected output: [1007, 1008, 1009, 1010]
'''

import re
data= "1007 Lakshman 1008 Karthik 1009-Ramesh -1010 Suresh"
lst = re.findall("\d{4}",data)
print(lst)