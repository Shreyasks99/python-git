'''1.	Given a string “12, 14-15,  18, 23- 2”, produce the list “[12, 14, 15, 18, 23, 2]”.'''

import re
data = "12, 14-15,  18, 23- 2"
lst = re.sub("[ -. ]"," ",data)   
print(lst)
