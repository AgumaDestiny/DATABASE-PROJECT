import csv
from cs50 import SQL
open("studentslist.db","w").close()
db=SQL("sqlite:///studentslist.db")
db.execute("CREATE TABLE student(id INTEGER, names TEXT, intake_student TEXT, sex TEXT, PRIMARY KEY(id), FOREIGN KEY(intake_student) REFERENCES intakes(intake))")
db.execute("CREATE TABLE intakes(id INTEGER, intake TEXT, number_students INTEGER, PRIMARY KEY(id))")
db.execute("CREATE TABLE entrance(student_id INTEGER, intake_id INTEGER, FOREIGN KEY(intake_id) REFERENCES intakes(id),FOREIGN KEY(student_id) REFERENCES student(id))")
db.execute("CREATE TABLE department(id INTEGER, departments TEXT, intake_id_available INTEGER, PRIMARY KEY(id),FOREIGN KEY(intake_id_available) REFERENCES intakes(id))")
db.execute("CREATE TABLE course(dept_id INTEGER, intake_id INTEGER, FOREIGN KEY(intake_id) REFERENCES intakes(id),FOREIGN KEY(dept_id) REFERENCES department(id))")

with open("STUDENTS LIST.csv", "r") as list:
    reader=csv.DictReader(list)

    for row in reader:
        index=row["id"]
        name=row["names"]
        intake_name=row["intake_student"]
        sex=row["sex"]
        student_id=row["student_id"]
        intake_id=row["intake_id"]
        number=row["id"]
        intake=row["intake"]
        total_students=row["number_students"]
        dept_no=row["dept_no"]
        intake_id=row["intake_id"]
        no=row["id"]
        departments=row["departments"]
        available=row["intake_id_available"]

        db.execute("INSERT INTO student(id, names, intake_student, sex) VALUES(?,?,?,?);",index, name, intake, sex)
        db.execute("INSERT INTO intakes(id, intake, number_students) VALUES(?,?,?);",number, intake, total_students)
        db.execute("INSERT INTO entrance(student_id , intake_id) VALUES(?,?);",student_id , intake_id)
        db.execute("INSERT INTO department(id, departments, intake_id_available) VALUES(?,?,?);",no, departments, available)
        db.execute("INSERT INTO course(dept_no, intake_id) VALUES(?,?)",dept_no, intake_id)

