from employee import Employee

lst_emp= []

def load_emp():
    with open("empdata.txt") as f:
        fdata = f.readlines()
        for data in fdata:
            edata = data.strip("\n").split(",")
            empno = int(edata[0])
            ename = edata[1]
            qual = edata[2]
            salary = edata[3]
            dept_name = edata[4]
            emp = Employee(empno,ename,qual,salary,dept_name)
            lst_emp.append(emp)
        print(f"Total Employee's count:{len(lst_emp)}")

def showDeptName():
    dnames = set(map(lambda emp:emp.dept_name,lst_emp))
    print("All Departments are:")
    for name in dnames:
        print(name)
    
def showQual():
    dqual = set(map(lambda emp:emp.qual,lst_emp))
    print("All Qualifications are:")
    for quali in dqual:
        print(quali)

def maxSalaryemp():
    print("Maximum Salary:")
    max_sal = max(list(map(lambda x:x.salary,lst_emp)))
    lst=[]
    lst= list(filter(lambda x:x.salary == max_sal,lst_emp))
    for emp in lst:
        emp.showInfo()

def showEmpCountByDeptName():
    pass

def showTotalSalByDeptName():
    pass

def showEmpCountByQual():
    pass



load_emp()
showDeptName()
showQual()
maxSalaryemp()
