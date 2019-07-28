try:
    w_count = {}
    #conj = ["if","but","and"]
    with open("data_1.txt") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split(",")
            for word in words:
                word = word.strip().strip("\n").replace(",","").replace(".","")
                try:
                    w_count[word] +=1
                except KeyError:
                    w_count[word] = 1
        '''max_val = max(w_count.values())
        for k,v in w_count.items():
            if v == max_val:
                print(f"{k} : {v}")
'''
    print(w_count)



finally:
    f.close()