try:
    word_count = 0
    with open("data.txt") as fin ,open("u_data.txt","w") as fout:
        lines = fin.readline()
        line_count = len(lines)
        for line in lines:
            word_count += len(line.split(","))
            print(line,end= "")
        print(f"Line Count is {line_count}")
        print(f"Word count is {word_count}")

        lines_1 = fin.readlines()
        lines_1 = [l.upper() for l in lines]
        fout.writelines(lines_1)

except Exception as e:
    print(f"File not found please check the path {e}")