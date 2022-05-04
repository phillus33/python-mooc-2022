if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

students = {}

with open(student_info) as new_file:
    for line in new_file:
        line = line.strip()

        parts = line.split(";")

        if parts[0] == "id":
            continue
        
        students[parts[0]] = parts[1] + " " + parts[2]

grades = {}

with open(exercise_data) as new_file:
    for line in new_file:
        line = line.strip()

        parts = line.split(";")

        if parts[0] == "id":
            continue
        
        # grades[parts[0]] = parts[1:]

        gsum = 0
        for grade in parts[1:]:
            gsum += int(grade)
        grades[parts[0]] = gsum

# for id, name in students.items():
#     if id in grades:
#         sumnum = 0
#         for grade in grades[id]:
#             sumnum += int(grade)
#     print(f"{name} {sumnum}")

for student_id, name in students.items():
    print(f"{name} {grades[student_id]}")
