import csv

data_lst = [
    {"id":1001,"Wname":"Python","year":2019,"Status":1,"Company":"Heraizen"},
    {"id":1001,"Wname":"Web","year":2019,"Status":1,"Company":"Heraizen"},
]

try:
    with open("ws.csv","w",newline='') as file:
        headings = ["ID","Wname","Year","Status","Company"]
        obj = csv.DictWriter(file,fieldnames = headings)
        obj.writeheader()
        obj.writerow(data_lst)

except Exception as e:
    print(str(e))