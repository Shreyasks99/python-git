import time
import random as rn
import dbcontext as db
from models import Internship 
from models import Student
from models import Company
from models import Student_count
from models import Student_report
from beautifultable import BeautifulTable

def _get_new_id():
    t_obj = time.localtime()
    new_id = rn.randint(1000,9900) + (t_obj.tm_min + t_obj.tm_hour + t_obj.tm_sec)
    return new_id

def add_internship(iname,company,i_year):
    id = _get_new_id()
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("insert into internship(id,iname,company,i_year,status) values(?,?,?,?,?)",(id,iname,company,i_year,1))
            print(f"Internship is added successfully with id:{id}")
    except Exception as e:
        print(str(e))

def view_all_internships():
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select id,iname,company,i_year,status from internship")
            rows = cursor.fetchall()
            intern_pro_lst = [Internship(*row) for row in rows]
            _view_internship_list(intern_pro_lst)
    except Exception as e:
        print(str(e))

def search_internship_by_name(name):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select * from internship where iname=?",(name,))
            row= cursor.fetchone()
            intern_pro_lst = [Internship(*row)]
            _view_internship_list(intern_pro_lst)

    except Exception as e:
        print(str(e))

def change_status_internship(id,status):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("update internship set status=? where id = ?",(status,id,))
            print(f"Status updated")
    except Exception as e:
        print(str(e))
    
def delete_internship(name):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("delete from internship where iname=?",(name,))
    except Exception as e:
        print(str(e))

def add_student_internship(name,sem):
    id = _get_new_id()
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("insert into student(usn,name,sem,placed) values(?,?,?,?)",(id,name,sem,1))
            print(f"Student is added successfully with id:{id}")
    except Exception as e:
        print(str(e))

def view_all_reg_student():
        try:
            with db.DbContext() as connection:
                cursor = connection.cursor()
                cursor.execute("select usn,name,sem,placed from student")
                rows = cursor.fetchall()
                intern_pro_lst = [Student(*row) for row in rows]
                _view_student_list(intern_pro_lst)
        except Exception as e:
            print(str(e))

def search_student_by_name(name):
    try:
        with db.DbContext() as connection:
                cursor = connection.cursor()
                cursor.execute("select * from student where name=?",(name,))
                row= cursor.fetchone()
                intern_pro_lst = [Student(*row)]
                _view_student_list(intern_pro_lst)
    except Exception as e:
        print(str(e))

def update_student(id,status):
        try:
            with db.DbContext() as connection:
                cursor = connection.cursor()
                cursor.execute("update student set placed=? where usn = ?",(status,id,))
                print(f"Status updated")
        except Exception as e:
                print(str(e))
    
def delete_student(name):
    try:
        with db.DbContext() as connection:
                cursor = connection.cursor()
                cursor.execute("delete from student where name=?",(name,))
    except Exception as e:
        print(str(e))
                
def company_ws_count(name):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select company,count(*) from internship where company=?",(name,))
            rows = cursor.fetchall()
            intern_pro_lst = [Company(*row) for row in rows]
            _view_comp_count_list(intern_pro_lst)
            
    except Exception as e:
        print(str(e))


def student_ws_count(stu):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select r.iid,usn,iname,company,count(*) from registration r inner join internship i on r.iid = i.id where usn=?",(stu,))
            rows = cursor.fetchall()
            if rows:
                intern_pro_lst = [Student_count(*row) for row in rows]
                _view_stu_count_list(intern_pro_lst)
            else:
                    print("No student to be displayed")

    except Exception as e:
        print(str(e))

    
def ws_student_reports(name):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select name,s.usn,sem,i.iname,i.company from student s inner join internship i inner join registration r on r.iid = i.id where name=?",(name,))
            rows = cursor.fetchall()
            if rows:
                intern_pro_lst = [Student_report(*row) for row in rows]
                _view_stu_report_list(intern_pro_lst)
            else:
                    print("No reports to be displayed")
            
    except Exception as e:
        print(str(e))


def reg_stu_internship(iid,usn):
     try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("insert into registration(iid,usn,status) values(?,?,?)",(iid,usn,0))
            print(f"Student {usn} is added successfully with iid:{iid}")
     except Exception as e:
        print(str(e))

def update_stu_intership_status(usn,status):
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("update registration set status=? where usn= ?",(status,usn,))
            print(f"Status updated")
    except Exception as e:
        print(str(e))


def _view_internship_list(lst):
    if lst and len(lst) > 0:
        table = BeautifulTable()
        table.column_headers = ["ID", "NAME", "COMPANAY", "YEAR","STATUS"]
        for l in lst:
            status = "Completed" if l.status == 0 else "Going on" 
            table.append_row([l.id, l.iname, l.company, l.i_year,status])
        print(table)
    else:
        print(f"There are no Intership programms, yet to add...")

def _view_student_list(lst):
    if lst and len(lst) > 0:
        table = BeautifulTable()
        table.column_headers = ["USN", "NAME", "SEM","STATUS"]
        for l in lst:
            table.append_row([l.usn,l.name,l.sem,l.placed])
        print(table)
    else:
        print(f"There is no students to be displayed")

def _view_comp_count_list(lst):
    if lst and len(lst) > 0:
        table = BeautifulTable()
        table.column_headers = ["COMPANY","COUNT"]
        for l in lst:
            table.append_row([l.company,l.count])
        print(table)
    else:
        print(f"There is no students to be displayed")

def _view_stu_count_list(lst):
    if lst and len(lst) > 0:
        table = BeautifulTable()
        table.column_headers = ["INTERN_ID","USN","INTERN_NAME","COMANPY","COUNT"]
        for l in lst:
            table.append_row([l.id,l.usn,l.iname,l.company,l.count])
        print(table)
    else:
        print(f"There is no students to be displayed")

def _view_stu_report_list(lst):
    if lst and len(lst) > 0:
        table = BeautifulTable()
        table.column_headers = ["NAME","USN","SEM","INTERN_NAME","COMPANY"]
        for l in lst:
            table.append_row([l.name,l.usn,l.sem,l.iname,l.company])
        print(table)
    else:
        print(f"There is no students to be displayed")