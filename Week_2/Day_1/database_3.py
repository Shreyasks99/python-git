''' Load data into json file'''
import json

data_lst = [
    {"id":1001,"Wname":"Python","year":2019,"Status":1,"Company":"Heraizen"},
    {"id":1001,"Wname":"Web","year":2019,"Status":1,"Company":"Heraizen"},
]

try:
    with open("ws.json","w",newline='') as file:
        json.dump(data_lst,file,indent = 4)

except Exception as e:
    print(str(e))