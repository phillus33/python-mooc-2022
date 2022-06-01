from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    return reduce(lambda reduce_sum, item: reduce_sum + item.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    return reduce(lambda reduce_sum, item: reduce_sum + item.credits, filter(lambda t: t.grade > 0, attempts), 0)

def average(attempts: list):
    return reduce(lambda reduce_sum, item: reduce_sum + item.grade, filter(lambda t: t.grade > 0, attempts), 0) / len(list(filter(lambda t: t.grade > 0, attempts)))


if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)