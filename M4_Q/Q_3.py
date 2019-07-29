from openpyxl import Workbook
import openpyxl as pyxl

def grade_point_from_letter(l):
    l_s_map = {"S":9,"S+":10,"O":10,"A":8,"B":7,"C":6,"E":5,"F":0}
    return l_s_map[l.strip()]

wb = pyxl.load_workbook("Student.xlsx")
sheet = wb.active
for row in sheet.iter_rows(min_row=3,min_col=2,max_col=13):
    if row:
        data = [c.value for c in row]
        stu= data[:2]
        sub_1 = data[5:7]
        sub_2 = data[-2:]
        student = [sub_1,sub_2]

        c_1 = sub_1[0]
        g_1 = grade_point_from_letter(sub_1[1])

        c_2= sub_2[0]
        g_2 = grade_point_from_letter(sub_2[1])

        si = ((c_1 * g_1) * (c_2 * g_2))/(c_1 + c_2)

    print(f"{si}")


