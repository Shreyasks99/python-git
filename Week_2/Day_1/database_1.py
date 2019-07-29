''' Write data into TEXT file'''
data_lst = [
    {"id":1001,"Wname":"Python","year":2019,"Status":1,"Company":"Heraizen"},
    {"id":1001,"Wname":"Python","year":2019,"Status":1,"Company":"Heraizen"}
]

try:
    with open("ws.txt","w") as file:
        for d in data_lst:
            line = f'{d["id"]},{d["Wname"]},{d["year"]},{d["Status"]},{d["Company"]}\n'
            file.write(line)

except Exception as e:
    print(str(e))