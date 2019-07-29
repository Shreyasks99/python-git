from openpyxl import Workbook
import openpyxl as pyxl

l_s_map = {"S":9,"S+":10,"O":10,"A":8,"B":7,"C":6,"E":5,"F":0}

class Student:
    def __init__(self,usn,name):
        self.usn = usn
        self.name = name
        self.subjects = []
    
    def show_sgpa_info(self):
        s_c =0
        g_c = 0
        for s in self.subjects:
            g_c += s["C"] * l_s_map[s["G"]]
            s_c += s["C"]
        si = g_c/s_c
        print(f"Name:{self.name} SGPA:{si}")

wb = pyxl.load_workbook("Student.xlsx")
sheet = wb.active
students = []
for row in sheet.iter_rows(min_row=3,min_col=2,max_col=13):
    if row:
        data = [c.value for c in row]
        stu= data[:2]
        sub_1 = data[5:7]
        sub_2 = data[-2:]
        student = [sub_1,sub_2]
        student = Student(*stu)
        student.subjects.append({"C":sub_1[0],"G":sub_2[1]})
        student.subjects.append({"C":sub_2[0],"G":sub_2[1]})
        students.append(student)

for s in students:
    s.show_sgpa_info()



        