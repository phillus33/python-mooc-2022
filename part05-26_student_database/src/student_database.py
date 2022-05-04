##### Version 1: using a dict to add student to students dict

def add_student(students: dict, name: str):

    students[name] = {}
    
    

def print_student(students: dict, name: str):

    if name not in students:
        print(f"{name}: no such person in the database")
        return
    
    students_completed_courses = students[name]
    print(f"{name}:")
    if len(students_completed_courses) == 0:
        print(" no completed courses")
    else:
        print(f" {len(students_completed_courses)} completed courses: ")
        sum = 0
        for course, grade in students_completed_courses.items():
            print(f"  {course} {grade}")
            sum += grade
        
        print(f" average grade {sum/len(students_completed_courses):.1f}")

def add_course(students: dict, name: str, course: tuple):
    courses = students[name]

    if course[1] == 0:
        return
    if course[0] in courses:
        if courses[course[0]] > course[1]:
            return
    courses[course[0]] = course[1]
    # print(courses)

def summary(students: dict): 

    print(f"students {len(students)}")
    
    
    most_courses_count  = 0
    
    best_avg_grade = 0

    

    for name, completions in students.items():
        # print(f"NAME: {name}, COMPLETIONS: {completions}")
        if len(completions) > most_courses_count :
            most_courses = name
            most_courses_count  = len(completions)
        
        sum = 0
        for course, grade in completions.items():
            sum += grade
        if len(completions) == 0:
            avg = 0
        else:
            avg = sum/len(completions)
        
        if avg > best_avg_grade:
            best_avg_grade = avg
            best = name

    print(f"most courses completed {most_courses_count} {most_courses}")
    print(f"best average grade {best_avg_grade:.1f} {best}")



##### Version 2: using a list to save a student to students dict

# def add_student(students: dict, name: str):
    # students[name] = []

# def print_student(students: dict, name: str):
    # exists = False
    # sum = 0
    # for key in students:
    #     if key == name:
    #         print(f"{name}: ")
    #         if students[key] == []:
    #             print(" no completed courses")
    #         else:
    #             # print(f"{name}: ")
    #             print(f" {len(students[key])} completed courses: ")
                
    #             for course in students[key]:
    #                 print(f"  {str(course[0])} {str(course[1])}")
    #                 sum += int(course[1])
    #             print(f" average grade {sum/len(students[key])}")
            
    #         exists = True
    # if not exists:
    #     print(f"{name}: no such person in the database")

    
# def add_course(students: dict, name: str, course: tuple):
#     if course[1] > 0:
#         if course[0] in str(students[name]): 
#             for taken_course in students[name]:
#                 if course[0] == taken_course[0] and course[1] > taken_course[1]:
#                     students[name].remove(taken_course)
#                     students[name].append(course)
            
#         else:
#             students[name].append(course)

# def summary(students: dict):
#     print(f"students {len(students)}")

#     most_nr = 0
#     most_name = ""
#     avg_grades = {}
#     for key in students:
#         sum = 0
#         if len(students[key]) > most_nr:
#             most_nr = len(students[key])
#             most_name = key
#         for course in students[key]:
#             sum += int(course[1])
#         avg_grades[key] = sum/len(students[key])

#     print(f"most courses completed {most_nr} {most_name}")
    
#     best_nr = 0
#     best_name = ""
#     for key in avg_grades:
#         if avg_grades[key] > best_nr:
#             best_nr = avg_grades[key]
#             best_name = key

#     print(f"best average grade {best_nr} {best_name}")

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 5))
# print_student(students, "Peter")    

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# add_course(students, "Peter", ("Data Structures and Algorithms", 0))
# add_course(students, "Peter", ("Introduction to Programming", 4))
# add_course(students, "Peter", ("Advanced Course in Programming", 5))
# print_student(students, "Peter")
# print("---------------")
# print(students["Peter"])



# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# print_student(students, "Peter")
# print_student(students, "Eliza")
# print_student(students, "Jack")

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# print_student(students, "Peter")

                

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Software Development Methods", 5))
# add_course(students, "Peter", ("Software Development Methods", 1))
# print_student(students, "Peter")