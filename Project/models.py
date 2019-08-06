from collections import namedtuple

Internship = namedtuple("Intership", ["id","iname", "company", "i_year","status"])
Student = namedtuple("Student", ["usn", "name", "sem","placed"])
Registration = namedtuple("Registration",["iid","usn","status"])
Company = namedtuple("Company",["company","count"])
Student_count = namedtuple("Stu_count",["id","usn","iname","company","count"])
Student_report = namedtuple("Stu_report",["name","usn","sem","iname","company"])