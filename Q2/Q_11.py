#11.	Following are the initials of players who play various games. Some of these players play more than one game.Cricket: [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"] Football: [ "PKM", "ALN","RMZ","CS", "MCS"] Badminton: [ "PKM", "ALN", "NV", "KM","RMV"]
#Write a program to:#
#a.	List those players who play all three games.#
#b.	List those players who play exactly one game.#
Cricket = "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"
Football = "PKM", "ALN","RMZ","CS", "MCS"
Badminton = "PKM", "ALN", "NV", "KM","RMV"
lst=[]
lst.extend(Cricket)
for name in Football:
    if name in lst:
        continue
    else:
        lst.append(name)
for name in Badminton:
    if name in lst:
        continue
    else:
        lst.append(name)
print(lst)