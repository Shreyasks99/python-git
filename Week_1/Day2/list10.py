data = "raj,siva,Mani,sonu,Anu,Tanvi"
x=list(map(lambda x:x.capitalize(),data.split(",")))
print(list(filter(lambda x : x.startswith("A"),x)))