def split_input(list: list):
    space = list.find(" ")
    exam = int(list[:space])
    exercise = int(list[space+1:])
    return [exam, exercise]

def actual_bonus(amount: int):
    return amount // 10

def grade(total_points: int):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if total_points >= boundary[i]:
            return i

def mean(points: list):
    return sum(points)/len(points)

def main():
    points = []
    grades = [0] * 6

    while True:
        answer = input("Exam points and exercises completed: ")
        if len(answer) == 0:
            break
        split_answer = split_input(answer)
        exercise_bonus = actual_bonus(split_answer[1])
        total_points = split_answer[0] + exercise_bonus

        points.append(total_points)
        grd = grade(total_points)
        if split_answer[0] < 10:
            grd = 0
        grades[grd] += 1

    pass_perc = 100*(len(points)-grades[0])/len(points)

    print("Statistics: ")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_perc:.1f}")
    print("Grade distribution: ")
    for i in range(5, -1, -1):
        print(f"  {i}: {'*'*grades[i]}")

main()