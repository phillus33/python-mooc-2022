if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

students = {}

with open(student_info) as new_file:
    for line in new_file:
        line = line.strip()

        parts = line.split(";")

        if parts[0] == "id":
            continue
        
        students[parts[0]] = parts[1] + " " + parts[2]

exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        line = line.strip()

        parts = line.split(";")

        if parts[0] == "id":
            continue
        
        gsum = 0
        for grade in parts[1:]:
            gsum += int(grade)
        exercises[parts[0]] = gsum

exams = {}

with open(exam_data) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        
        if parts[0] == "id":
            continue

        esum = 0
        for score in parts[1:]:
            esum += int(score)
        exams[parts[0]] = esum

# print(exams)


for student_id, name in students.items():
    final_score = (exercises[student_id]//4) + exams[student_id]
    # if final_score > 0 and final_score < 15:
    #     grade = 0
    # elif final_score > 14 and final_score < 18:
    #     grade = 1
    # elif final_score > 17 and final_score < 21:
    #     grade = 2
    # elif final_score >= 21 and final_score <= 23:
    #     grade = 3
    # elif final_score >= 24 and final_score <= 27:
    #     grade = 4
    # elif final_score >= 28:
    #     grade = 5
    grade = 0
    limits = [15, 18, 21, 24, 28]
    while grade < 5 and final_score >= limits[grade]:
        grade += 1
    print(f"{name} {grade}")