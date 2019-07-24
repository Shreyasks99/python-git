class Employee:
    def __init__(self,emp_no,e_name,qual,salary,dept_name):
        self.emp_no = emp_no
        self.e_name = e_name
        self.qual = qual
        self.salary = salary
        self.dept_name =  dept_name

    def showInfo(self):
        print(f"{self.emp_no} - {self.e_name} - {self.qual} - {self.salary}- {self.dept_name}")
    
    def increment_salary(self,inc_amount):
        self.salary += inc_amount
        print(f"{self.e_name}:salary after increment {self.salary}")