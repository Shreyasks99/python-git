''' Load data to Excel'''
from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
data = [
    ('id','wname','year','status','company'),
    (1001,"Python",2019,1,"Heraizen"),
    (1002,"Web",2018,0,"Spaneos")
]
for row in data:
    sheet.append(row)
wb.save("Student.xlsx")

