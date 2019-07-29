''' Load data into TEXT file'''
data_lst = [
    [1001,"Python",2019,1,"Heraizen"],
    [1002,"Web",2018,1,"Spaneos"],
    [1003,"Java",2020,1,"Heraizen"]
            ]       

try:
    with open("ws.txt","w") as file:
        for d in data_lst:
            line = f'{d[0]},{d[1]},{d[2]},{d[3]},{d[4]}\n'
            file.write(line)

except Exception as e:
    print(f"File not found {e}")