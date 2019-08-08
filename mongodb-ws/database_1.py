import database as db

while True:
    print("1.Add new Faculty 2.Add Subjects to faculty 3.Delete subjects from faculty 4.Increment Experience by one year 5.Update Qualification 6.Totalduration by faculty 7.Print Faculty with subjects 8.Delete faculty")
    ch = int(input("Enter the choice:"))
    if ch == 1:
        db.add_new_faculty()
    elif ch == 2:
        db.add_subject_to_faculty()
    elif ch == 3:
        db.delete_subject_from_faculty()
    elif ch == 4:
        db.increment_exp_by_one_year()
    elif ch == 5:
        db.update_qualification()
    elif ch == 6:
        db.total_duration_by_faculty()
    elif ch == 7:
        db.subject_with_faculty_name()
    elif ch == 8:
        db.delete_faculty()
    else:
        exit(0)

    

