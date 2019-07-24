names =["PKM","ALN","PVR","PKM","ALN","GLN","NVR","PVR","KM","VP","CS","MCS"]
c_name={}
for name in names:
    if c_name.get(name) == None:
        c_name[name]=1
    else:
        c_name[name]=c_name[name]+1
print(c_name)