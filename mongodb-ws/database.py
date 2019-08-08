import pymongo

conn = pymongo.MongoClient('mongodb://localhost:27017/')
db= conn['mite']
collec=db['faculty']

def add_new_faculty():
    name = input("Enter the name:")
    age = int(input("enter the age:"))
    gender = input("Enter the gender:")
    exp = int(input("Enter the experience:"))
    qual = input("Enter the qualificaton:")
    sub_name = input("Enter the subjects he/she teaches:")
    duration = input("Enter the duraton of the faculty:")
    record_1 = {"name":name,"age":age,"gender":gender,"exp":exp,"qualification":qual,"subjects":[{"sub_name":sub_name,"duration":duration}]}
    collec.insert_one(record_1)
    print("Data inserted")

def add_subject_to_faculty():
    name = input("Enter the name of the faculty to whom subjects must be added:")
    sub_name= input("Enter the subjects to be added:")
    duration = input("Enter the duration:")
    collec.update_one({"name":name},{"$push":{"subjects":{"sub_name":sub_name,"duration":duration}}})
    print("Updated Succesfully")
    
def delete_subject_from_faculty():
    name = input("Enter the name of the faculty whose subjects must be deleted:")
    sub_name= input("Enter the subjects to be deleted:")
    collec.update_one({"name":name},{"$pull":{"subjects":{"sub_name":sub_name}}})
    print("Deleted successfully")
    
def increment_exp_by_one_year():
    collec.update_one({"name":"Krathi"},{"$inc":{"exp":1}})
    print("Updated Succesfully")

def update_qualification():
    collec.update_one({"name":"Krathi"},{"$push":{"qualification":"Ph.d"}})
    print("Updated Succesfully")

def total_duration_by_faculty():
    query = [
            { "$unwind":"$subjects"},
            { "$group":{"_id":"$name","t_hours":{"$sum":"$subject.duration"}}},
            { "$project":{"name":"$_id","t_hours":"$t_hours","_id":0}}
    ]
    res = collec.aggregate(query)
    for d in list(res):
        print(f"{d['name']} - {d['durations']}")

    
def subject_with_faculty_name():
    query = [
        {"$unwind":"$subjects"},
        {"$project":{"name":1,"subjects":"$subject.sub_name"}}
    ]
    res = collec.aggregate(query)
    for d in list(res):
        print(f"{d['name']} - {d['subject']}")

def delete_faculty():
    record_1 = {"name":"John"}  
    collec.delete_one(record_1)
    print("Faculty Deleted")

#add_new_faculty()
#delete_faculty()
#add_subject_to_faculty()
#update_qualification()
#subject_with_faculty_name()
#increment_exp_by_one_year()
#delete_subject_from_faculty()
#total_duration_by_faculty()
