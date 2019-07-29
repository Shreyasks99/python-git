def dictionary(student_dict):
    for a ,b in student_dict.items():
        print(f"{a}:{b}")

student_dict = {"101":"Rajesh","102":"Suresh","103":"Mahesh"}
dictionary(student_dict)