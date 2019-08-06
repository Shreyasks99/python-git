import pymongo

conn = pymongo.MongoClient('mongodb://localhost:27017/')
db= conn['mite']
collec=db['faculty']
def add_new_faculty():
    record_1 = {"name":"Faiz","age":20,"gender":"F","exp":11.5,"qualification":["BE"],"subjects":[{"sub_name":"Python","duration":40}]}
    collec.insert_one(record_1)
    print("Data inserted")

def add_subject_to_faculty():
    collec.update_one({"name":"Srinivas"},{"$push":{"subjects":"Machine Leaning"}})
    print("Updated Succesfully")
    
def delete_subject_from_faculty():
    collec.update_one({"name":"Srinivas"},{"$pull":{"subjects":"ENGLISH"}})
    print("Deleted successfully")
    
def increment_exp_by_one_year():
    collec.update_one({"name":"Krathi"},{"$inc":{"exp":1}})
    print("Updated Succesfully")

def update_qualification():
    collec.update_one({"name":"Krathi"},{"$push":{"qualification":"Ph.d"}})
    print("Updated Succesfully")

def total_duration_by_faculty():
    print(collec.aggregate([{"$group":{"_id":"null","res":{"$sum":"$duration"}}}]))
    
def subject_with_faculty_name():
    print(collec.find({},{"name":1,"subject":1}))

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
total_duration_by_faculty()
