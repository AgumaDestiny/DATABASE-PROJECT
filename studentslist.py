import csv
from cs50 import SQL
intakes = set()

open("studentslist.db","w").close()
db=SQL("sqlite:///studentslist.db")

db.execute("CREATE TABLE intakes(id INTEGER, intake TEXT, number_students INTEGER, PRIMARY KEY(id))")
db.execute("CREATE TABLE student(id INTEGER PRIMARY KEY AUTOINCREMENT, names TEXT, intake_id INTEGER,  sex TEXT, FOREIGN KEY(intake_id) REFERENCES intakes(id))")
db.execute("CREATE TABLE entrance(student_id INTEGER, intake_id INTEGER, FOREIGN KEY(intake_id) REFERENCES intakes(id),FOREIGN KEY(student_id) REFERENCES student(id))")
db.execute("CREATE TABLE department(department_id INTEGER, departments TEXT, intake_id_available INTEGER, PRIMARY KEY(id),FOREIGN KEY(intake_id_available) REFERENCES intakes(id))")
db.execute("CREATE TABLE course(dept_id INTEGER, intake_id INTEGER, FOREIGN KEY(intake_id) REFERENCES intakes(id),FOREIGN KEY(dept_id) REFERENCES department(department_id))")

with open("STUDENTS LIST.csv", "r") as list:
    reader=csv.DictReader(list)

    for row in reader:
        index=row["id"]
        name=row["names"]
        sex=row["sex"]
        intake=row["intake"]
        total_students=row["number_students"]
        no=row["department_id"]
        department=row["departments"]
        available=row["intake_id_available"]

        db.execute("INSERT INTO student(names, intake_id, sex) VALUES(?,(SELECT id FROM intakes WHERE intake = ?),?);", name, available, sex)
        db.execute("INSERT INTO intakes(intake, number_students) VALUES(?,?);", intake, total_students)
        db.execute("INSERT INTO entrance(student_id , intake_id) VALUES((SELECT id FROM student WHERE names = ?),(SELECT id FROM intakes WHERE intake = ?));",name, intake)
        db.execute("INSERT INTO department(departments, intake_id_available) VALUES(?,(SELECT id FROM intakes WHERE intake = ?));",department, intake)
        db.execute("INSERT INTO course(dept_id, intake_id) VALUES((SELECT id FROM department WHERE departments = ?),(SELECT id FROM intakes WHERE intake = ?))",department, intake)