import json
try:
    with open("ws.json","r") as file:
        ws_lst = json.load(file)
        for w in ws_lst:
            print(f"ID:{w['Id']} Name:{w['Wname']} Year:{w['Year']} Status:{w['Status']} Company:{w['Company']}")

except Exception as e:
    print(str(e))