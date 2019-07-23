data = "Aln,gln,Suresh,Ramesh,Akash,Shreyas,Faiz,Anand,Abhinav,mahesh,Dinesh,Sharukh,Khan,Salman,Katrina,Karenna"
lst=[]
names=data.upper().split(",")
for name in names:
    if name.startswith("A") or name.endswith("H"):
        lst.append(name)
lst.sort()
print(lst)