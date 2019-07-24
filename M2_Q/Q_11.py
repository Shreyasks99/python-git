#11.	Following are the initials of players who play various games. Some of these players play more than one game.Cricket: [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"] Football: [ "PKM", "ALN","RMZ","CS", "MCS"] Badminton: [ "PKM", "ALN", "NV", "KM","RMV"]
#Write a program to:#
#a.	List those players who play all three games.#
#b.	List those players who play exactly one game.#
Cricket = "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"
Football = "PKM", "ALN","RMZ","CS", "MCS"
Badminton = "PKM", "ALN", "NV", "KM","RMV"
lst=[]
print("Player who plays in all the games:")
for i in Cricket:
    if i in Football and i in Badminton:
        print(i)
lst.extend(Cricket)
lst.extend(Football)
lst.extend(Badminton)

list_1 = {}

for name in lst:
    if not name in list_1:
        list_1[name] = 1
    else:
        list_1[name] += 1

print("Players who are playing only in one game:")
for name_1 in lst:
    if list_1[name_1] == 1:
        print(name_1)
